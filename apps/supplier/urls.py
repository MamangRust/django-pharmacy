from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierEditView,
    SupplierDeleteView,
)


urlpatterns = [
    path("", SupplierListView.as_view(), name="supplier_list"),
    path("create/", SupplierCreateView.as_view(), name="supplier_create"),
    path("update/<int:id>", SupplierEditView.as_view(), name="supplier_update"),
    path("delete/<int:id>", SupplierDeleteView.as_view(), name="supplier_delete"),
]
