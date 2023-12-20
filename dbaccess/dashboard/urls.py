from django.urls import path
from dashboard import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/admin/", views.admin, name="admin_dashboard"),
]
