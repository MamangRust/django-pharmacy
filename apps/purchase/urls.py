from django.urls import path
from .views import (
    PurchaseListView,
    PurchaseCreateView,
    PurchaseEditView,
    PurchaseDeleteView,
    PurchaseReportView,
)

urlpatterns = [
    path("", PurchaseListView.as_view(), name="purchase_list"),
    path("create/", PurchaseCreateView.as_view(), name="purchase_create"),
    path("update/<int:id>", PurchaseEditView.as_view(), name="purchase_update"),
    path("delete/<int:id>", PurchaseDeleteView.as_view(), name="purchase_delete"),
    path("generate-pdf/", PurchaseReportView.as_view(), name="purchase_generate_pdf"),
]
