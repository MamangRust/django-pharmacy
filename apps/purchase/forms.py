from django import forms
from .models import Purchase
from apps.category.models import Category
from apps.supplier.models import Supplier


class PurchaseForm(forms.ModelForm):
    product = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    cost_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    quantity = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    expiry_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"})
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Purchase
        fields = [
            "product",
            "category",
            "supplier",
            "cost_price",
            "quantity",
            "expiry_date",
            "image",
        ]
