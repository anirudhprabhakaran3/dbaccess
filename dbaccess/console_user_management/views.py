from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from console_user_management.forms import (
    CustomUserCreationForm,
    RoleCreationForm,
    UserRoleAssignmentForm,
    UserSelectionForm,
    CustomUserChangeForm,
    RoleSelectionForm,
)
from console_user_management.models import (
    User,
    Role,
    UserRoleAssignment
)

from console_user_management.serializers import user_role_assignment_serializer


# Create your views here.
@login_required
def index(request):
    return render(request, "console_user_management/index.html")


@login_required
def user_creation(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User added successfully.")
            return redirect("user_creation")
    args = {"form": form}

    return render(request, "console_user_management/user_creation.html", args)


@login_required
def role_creation(request):
    form = RoleCreationForm()
    if request.method == "POST":
        form = RoleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Role created successfully!")
            return redirect("role_creation")

    args = {"form": form}
    return render(request, "console_user_management/role_creation.html", args)


@login_required
def user_role_assignment(request):
    form = UserRoleAssignmentForm()
    if request.method == "POST":
        form = UserRoleAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Association created successfully!")
            return redirect("user_role_assignment")
    args = {"form": form}

    return render(request, "console_user_management/user_role_assignment.html", args)


@login_required
def user_modification(request):
    form = UserSelectionForm()
    if request.method == "POST":
        form = UserSelectionForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            return redirect("user_modification_form", pk=user.pk)
        else:
            return render(
                request, "console_user_management/user_selection.html", {"form": form}
            )
    args = {"form": form}
    return render(request, "console_user_management/user_selection.html", args)


@login_required
def user_modification_form(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = CustomUserChangeForm(instance=user)

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f"User {user.email} modified successfully!")
            return redirect("user_modification")
        else:
            return render(
                request, "console_user_management/user_selection.html", {"form": form}
            )
    args = {"form": form}
    return render(request, "console_user_management/user_modification_form.html", args)


@login_required
def user_deletion(request):
    form = UserSelectionForm()
    if request.method == "POST":
        form = UserSelectionForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            user.delete()
            messages.success(request, "User deleted successfully.")
            return redirect("user_deletion")
    args = {"form": form}

    return render(request, "console_user_management/user_deletion.html", args)


@login_required
def role_deletion(request):
    form = RoleSelectionForm()
    if request.method == "POST":
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get("role")
            role.delete()
            messages.success(request, "Role deleted successfully!")
            return redirect("role_deletion")
        else:
            args = {"form": form}
            return render(request, "console_user_management/role_deletion.html", args)
    args = {"form": form}

    return render(request, "console_user_management/role_deletion.html", args)


@login_required
def role_modification(request):
    form = RoleSelectionForm()
    if request.method == "POST":
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get("role")
            return redirect("role_modification_form", pk=role.pk)
        else:
            print(form.errors)
            return render(
                request, "console_user_management/role_selection.html", {"form": form}
            )
    args = {"form": form}
    return render(request, "console_user_management/role_selection.html", args)


@login_required
def role_modification_form(request, pk):
    role = get_object_or_404(Role, pk=pk)
    form = RoleCreationForm(instance=role)

    if request.method == "POST":
        form = RoleCreationForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, "Role Modified Successfully!")
            return redirect("role_modification")

    args = {
        "form": form
    }

    return render(request, "console_user_management/role_modification_form.html", args)


@login_required
def edit_user_role_association(request):
    users = User.objects.all()
    args = {
        "users": users,
    }
    return render(request, "console_user_management/edit_user_role_association.html", args)


@login_required
def get_role_assignments_from_user_id(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user = User.objects.get(pk=user_id)
        assignments = UserRoleAssignment.objects.filter(user=user)

        if request.POST.get("role_id") is not None:
            role = Role.objects.get(pk=request.POST.get("role_id"))
            assignments = assignments.filter(role=role)

        assignments = user_role_assignment_serializer(assignments)
        return JsonResponse({"data": assignments})


@login_required
def update_user_role_assignment(request):
    if request.method == "POST":
        user_id = request.POST.get("users")
        role_id = request.POST.get("roles")
        expiry_date = request.POST.get("expiry_date")
        expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%dT%H:%M")

        user = User.objects.get(pk=user_id)
        role = Role.objects.get(pk=role_id)
        assignment = UserRoleAssignment.objects.get(user=user, role=role)

        assignment.expiry_date = expiry_date
        assignment.save()

        messages.success(request, "Updated association")
        return redirect("edit_user_role_association")
