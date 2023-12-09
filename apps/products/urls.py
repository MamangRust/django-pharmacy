from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductEditView,
    ProductDeleteView,
    ProductExpiredView,
    ProductOutStockView,
)

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("update/<int:id>", ProductEditView.as_view(), name="product_update"),
    path("delete/<int:id>", ProductDeleteView.as_view(), name="product_delete"),
    path("expired", ProductExpiredView.as_view(), name="product_expired"),
    path("outstock", ProductOutStockView.as_view(), name="product_outstock"),
]
