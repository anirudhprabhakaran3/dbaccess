from django.urls import path
from console_user_management import views

urlpatterns = [
    path("", views.index, name="console_user_management"),
    path("user_creation/", views.user_creation, name="user_creation"),
    path("role_creation/", views.role_creation, name="role_creation"),
    path(
        "user_role_assignment/",
        views.user_role_assignment,
        name="user_role_assignment",
    ),
]
