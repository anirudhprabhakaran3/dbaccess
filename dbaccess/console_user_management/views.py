from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from console_user_management.forms import CustomUserCreationForm, RoleCreationForm


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
        form = RoleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Role added successfully.")
            return redirect("role_creation")

    form = RoleCreationForm()
    args = {
        "form": form
    }

    return render(request, "console_user_management/role_creation.html", args)
