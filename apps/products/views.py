from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
from django.http import JsonResponse
from datetime import date
from apps.purchase.models import Purchase
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm


# Create your views here.
class ProductListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        products = Product.objects.all().order_by("-created_at")
        return render(request, "admin/product/index.html", {"products": products})


class ProductCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        form = ProductForm()
        purchase = Purchase.objects.all()
        return render(
            request=request,
            template_name="admin/product/create.html",
            context={"purchase": purchase, "form": form},
        )

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            return JsonResponse({"message": "Product created successfully"}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)


class ProductEditView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request, id):
        purchase = Purchase.objects.all()
        product = get_object_or_404(Product, pk=id)
        form = ProductForm(instance=product)

        return render(
            request=request,
            template_name="admin/product/edit.html",
            context={"product": product, "purchase": purchase, "form": form},
        )

    def post(self, request, id):
        purchase = Purchase.objects.all()
        product = get_object_or_404(Product, pk=id)

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return JsonResponse({"message": "Product update successfully"}, status=201)
        else:
            errors = form.errors.as_json()

            return JsonResponse({"errors": errors}, status=400)


class ProductExpiredView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        products = Purchase.objects.filter(expiry_date=date.today())

        return render(
            request=request,
            template_name="admin/product/expired.html",
            context={"products": products},
        )


class ProductOutStockView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        products = Purchase.objects.filter(quantity__lte=0)

        return render(
            request=request,
            template_name="admin/product/outstock.html",
            context={"products": products},
        )


class ProductDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)

        product.delete()

        return JsonResponse({"message": "Product deleted successfully"})
