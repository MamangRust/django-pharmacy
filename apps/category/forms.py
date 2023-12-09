from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label="Nama Kategori",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Name isi...",
                "data-parsley-required": "true",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "Nama Kategori"
        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["name"].widget.attrs["placeholder"] = "Name isi..."
        self.fields["name"].widget.attrs["data-parsley-required"] = "true"
        self.fields["name"].label_attrs = {"class": "form-label"}

    class Meta:
        model = Category
        fields = ["name"]
