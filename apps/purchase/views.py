from django.shortcuts import render, get_object_or_404
from apps.category.models import Category
from .models import Purchase
from django.views import View
from django.http import HttpResponse, JsonResponse

from django.template.loader import get_template
from weasyprint import HTML
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PurchaseForm
from apps.supplier.models import Supplier


class PurchaseListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        purchases = Purchase.objects.all()

        return render(
            request=request,
            template_name="admin/purchases/index.html",
            context={"purchases": purchases},
        )


class PurchaseCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        title = "create purchase"
        categories = Category.objects.all()
        suppliers = Supplier.objects.all()
        form = PurchaseForm()
        return render(
            request,
            "admin/purchases/create.html",
            {
                "title": title,
                "categories": categories,
                "suppliers": suppliers,
                "form": form,
            },
        )

    def post(self, request):
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse(
                {"message": "Purchase created successfully"}, status=201
            )
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


class PurchaseEditView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request, id):
        purchase = get_object_or_404(Purchase, pk=id)
        categories = Category.objects.all()  # Fetch all categories
        suppliers = Supplier.objects.all()  # Fetch all suppliers
        form = PurchaseForm(instance=purchase)

        return render(
            request,
            "admin/purchases/edit.html",
            {
                "title": "Edit Purchase",
                "purchase": purchase,
                "categories": categories,
                "suppliers": suppliers,
                "form": form,
            },
        )

    def post(self, request, id):
        purchase = get_object_or_404(Purchase, pk=id)
        categories = Category.objects.all()  # Fetch all categories
        suppliers = Supplier.objects.all()  # Fetch all suppliers
        form = PurchaseForm(request.POST, request.FILES, instance=purchase)

        if form.is_valid():
            form.save()

            return JsonResponse({"message": "Purchase update successfully"}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


class PurchaseDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def delete(self, request, id):
        purchase = get_object_or_404(Purchase, pk=id)
        purchase.delete()

        return JsonResponse({"message": "Purchase deleted successfully"})


class PurchaseReportView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def post(self, request):
        from_date = request.POST.get("from_date")
        to_date = request.POST.get("to_date")

        if from_date and to_date:
            purchases = Purchase.objects.filter(created_at__range=[from_date, to_date])
        else:
            purchases = Purchase.objects.all()

        template = get_template("admin/purchases/report.html")
        html = template.render({"purchases": purchases})

        pdf_file = HTML(string=html).write_pdf()

        response = HttpResponse(pdf_file, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="purchase_report.pdf"'
        return response
