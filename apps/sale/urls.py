from django.urls import path
from .views import (
    SaleListView,
    SaleCreateView,
    SaleEditView,
    SaleDeleteView,
    SaleReportView,
)

urlpatterns = [
    path("", SaleListView.as_view(), name="sale_list"),
    path("create/", SaleCreateView.as_view(), name="sale_create"),
    path("update/<int:id>", SaleEditView.as_view(), name="sale_update"),
    path("delete/<int:id>", SaleDeleteView.as_view(), name="sale_delete"),
    path("generate-pdf/", SaleReportView.as_view(), name="sale_generate_pdf"),
]
