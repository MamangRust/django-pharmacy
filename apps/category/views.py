from django.shortcuts import render, get_object_or_404, redirect
from .models import Category
from .forms import CategoryForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryIndexView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        categories = Category.objects.all()
        return render(request, "admin/category/index.html", {"categories": categories})


class CategoryCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def get(self, request):
        form = CategoryForm()
        return render(request, "admin/category/create.html", {"form": form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category-list")
        return render(request, "admin/category/create.html", {"form": form})


class CategoryUpdateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    template_name = "admin/category/edit.html"

    def get(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        form = CategoryForm(instance=category)
        return render(request, self.template_name, {"form": form, "category": category})

    def post(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("category-list")


class CategoryDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login"

    def post(self, request, category_id):
        category = get_object_or_404(Category, pk=category_id)
        category.delete()
        return redirect("category-list")
