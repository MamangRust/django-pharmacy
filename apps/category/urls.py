from django.urls import path
from .views import (
    CategoryIndexView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path("", CategoryIndexView.as_view(), name="category-list"),
    path("create/", CategoryCreateView.as_view(), name="create_category"),
    path(
        "update/<int:category_id>/",
        CategoryUpdateView.as_view(),
        name="update_category",
    ),
    path(
        "delete/<int:category_id>/",
        CategoryDeleteView.as_view(),
        name="delete_category",
    ),
]
