from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models import Sum
from apps.sale.models import Sale
from apps.user.models import User
from apps.purchase.models import Purchase
from apps.products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request):
        try:
            user_count = User.objects.count()
            product_count = Product.objects.count()
            sale_count = Sale.objects.count()
            yearly_revenue_decimal = self.calculate_yearly_revenue()
            yearly_revenue = [float(val) for val in yearly_revenue_decimal]
            total_cost_price = (
                Purchase.objects.all().aggregate(total_cost=Sum("cost_price"))[
                    "total_cost"
                ]
                or 0
            )

            total_revenue = sum(yearly_revenue)

            response_data = {
                "user": user_count,
                "product": product_count,
                "sale": sale_count,
                "yearly_revenue": yearly_revenue,
                "total_revenue": total_revenue,
                "total_cost_price": total_cost_price,
            }

            return render(
                request=request,
                template_name="admin/dashboard.html",
                context=response_data,
            )

        except Exception as err:
            return JsonResponse({"error": str(err)}, status=400)

    def calculate_yearly_revenue(self):
        yearly_revenue = []
        for month in range(1, 13):
            total_revenue = (
                Sale.objects.filter(created_at__month=month).aggregate(
                    total_revenue=Sum("total_price")
                )["total_revenue"]
                or 0
            )
            yearly_revenue.append(total_revenue)
        return yearly_revenue
