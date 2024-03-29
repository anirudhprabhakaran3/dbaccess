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
    path("user_modification/", views.user_modification, name="user_modification"),
    path(
        "user_modification/<int:pk>/",
        views.user_modification_form,
        name="user_modification_form",
    ),
    path("user_deletion/", views.user_deletion, name="user_deletion"),
    path("role_deletion/", views.role_deletion, name="role_deletion"),
    path("role_modification/", views.role_modification, name="role_modification"),
    path(
        "role_modification/<int:pk>",
        views.role_modification_form,
        name="role_modification_form",
    ),
    path("edit_user_role_association/", views.edit_user_role_association, name="edit_user_role_association"),
    path("user_role_association/update/", views.update_user_role_assignment, name="update_user_role_assignment"),
    path("user/assignments", views.get_role_assignments_from_user_id, name="user_assignments"),
    path("mass_update/", views.mass_update, name="mass_update"),
    path("reports/", views.reports, name="reports"),
    path("reports/user", views.reports_user, name="reports_user"),
    path("reports/role", views.reports_role, name="reports_role"),
]
