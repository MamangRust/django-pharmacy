from django.urls import path
from .views import UserListView, UserCreateView, UserEditView, UserDeleteView

urlpatterns = [
    path("", UserListView.as_view(), name="user_list"),
    path("create/", UserCreateView.as_view(), name="user_create"),
    path("update/<int:id>", UserEditView.as_view(), name="user_edit"),
    path("delete/<int:id>", UserDeleteView.as_view(), name="user_delete"),
]
