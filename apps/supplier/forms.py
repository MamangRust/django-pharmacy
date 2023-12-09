from django import forms
from .models import Supplier


class SupplierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    product = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    comment = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4})
    )

    class Meta:
        model = Supplier
        fields = ["name", "email", "phone", "company", "address", "product", "comment"]
