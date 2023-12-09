from django import forms
from .models import Product
from apps.purchase.models import Purchase


class ProductForm(forms.ModelForm):
    purchase = forms.ModelChoiceField(
        queryset=Purchase.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    discount = forms.DecimalField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"})
    )

    class Meta:
        model = Product
        fields = ["purchase", "price", "discount", "description"]
