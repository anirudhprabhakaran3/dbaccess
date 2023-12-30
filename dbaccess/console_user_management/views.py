from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from console_user_management.forms import CustomUserCreationForm, RoleCreationForm, RolePermissionAssignmentForm
from console_user_management.models import Permission, RolePermissionAssignment


# Create your views here.
@login_required
def index(request):
    return render(request, "console_user_management/index.html")


@login_required
def user_creation(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully.")
            return redirect("user_creation")

    form = CustomUserCreationForm()
    args = {
        "form": form
    }

    return render(request, "console_user_management/user_creation.html", args)


@login_required
def role_creation(request):
    if request.method == "POST":
        role_form = RoleCreationForm(request.POST)
        if role_form.is_valid():
            role = role_form.save()
            req_data = dict(request.POST)
            for (permission_name, permission_level) in zip(req_data.get("permission", None),
                                                           req_data.get("permission_level", None)):
                permission = Permission.objects.get(permission_name=permission_name)
                role_perm_assignment = RolePermissionAssignment(role=role, permission=permission,
                                                                permission_level=permission_level)
                role_perm_assignment.save()

            messages.success(request, "Role created and permissions set!")
            return redirect("role_creation")

    role_form = RoleCreationForm()
    role_perm_assignment_forms = []
    permissions = Permission.objects.all()
    for permission in permissions:
        role_perm_assignment_forms.append(
            RolePermissionAssignmentForm(initial={"permission": permission.permission_name}))

    args = {
        "role_form": role_form,
        "role_perm_assignment_forms": role_perm_assignment_forms
    }

    return render(request, "console_user_management/role_creation.html", args)
