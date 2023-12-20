from django.urls import path
from console_user_management import views

urlpatterns = [
    path("", views.index, name="console_user_management"),
    path("user_creation/", views.user_creation, name="user_creation")
]