from django import forms
from .models import Sale
from apps.products.models import Product
from apps.user.models import User


class SaleForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    quantity = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    total_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Sale
        fields = ["product", "quantity", "total_price", "user"]
