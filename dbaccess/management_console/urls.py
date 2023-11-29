from django.urls import path

from .views import home

urlpatterns = [
    path("", home, name="management_console_home"),
]