from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import JsonResponse
from .models import Supplier
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SupplierForm


# Create your views here.
class SupplierListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        suppliers = Supplier.objects.all()
        return render(request, "admin/suppliers/index.html", {"suppliers": suppliers})


class SupplierCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        title = "Create supplier"
        form = SupplierForm()

        return render(
            request=request,
            template_name="admin/suppliers/create.html",
            context={"title": title, "form": form},
        )

    def post(self, request):
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("supplier_list")
        else:
            return redirect("supplier_list")


class SupplierEditView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request, id):
        supplier = get_object_or_404(Supplier, pk=id)

        form = SupplierForm(instance=supplier)
        return render(
            request,
            "admin/suppliers/edit.html",
            {"supplier": supplier, "form": form},
        )

    def post(self, request, id):
        supplier = get_object_or_404(Supplier, pk=id)
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()

            return redirect("supplier_list")
        else:
            return redirect("supplier_list")


class SupplierDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def delete(self, request, id):
        supplier = get_object_or_404(Supplier, pk=id)
        supplier.delete()

        return JsonResponse({"message": "Supplier deleted successfully"})
