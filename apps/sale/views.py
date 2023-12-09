from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale
from apps.products.models import Product
from apps.user.models import User
from django.template.loader import get_template
from django.http import JsonResponse, HttpResponse
from django.views import View
from .forms import SaleForm
from django.contrib.auth.mixins import LoginRequiredMixin
from weasyprint import HTML


class SaleListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        sale = Sale.objects.all()

        return render(
            request=request,
            template_name="admin/sale/index.html",
            context={"sales": sale},
        )


class SaleCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        user = User.objects.all()
        product = Product.objects.all()
        form = SaleForm()

        return render(
            request=request,
            template_name="admin/sale/create.html",
            context={"user": user, "product": product, "form": form},
        )

    def post(self, request):
        form = SaleForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({"message": "Sale created successfully"}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


class SaleEditView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request, id):
        sale = get_object_or_404(Sale, pk=id)
        user = User.objects.all()
        product = Product.objects.all()
        form = SaleForm(instance=sale)

        return render(
            request=request,
            template_name="admin/sale/edit.html",
            context={"user": user, "product": product, "form": form, "sale": sale},
        )

    def post(self, request, id):
        sale = get_object_or_404(Sale, pk=id)
        form = SaleForm(request.POST, instance=sale)

        if form.is_valid():
            form.save()

            return JsonResponse({"message": "Sale update successfully"}, status=201)
        else:
            errors = form.errors.as_json()
            print(errors)
            return JsonResponse({"errors": errors}, status=400)


class SaleDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def delete(self, request, id):
        sale = get_object_or_404(Sale, pk=id)

        sale.delete()

        return JsonResponse({"message": "Sale deleted successfully"})


class SaleReportView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def post(self, request):
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")

        if from_date and to_date:
            sales = Sale.objects.filter(created_at__range=[from_date, to_date])
        else:
            sales = Sale.objects.all()

        template = get_template("admin/sale/report.html")
        html = template.render({"sales": sales})

        pdf_file = HTML(string=html).write_pdf()

        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="purchase_report.pdf"'
        return response
