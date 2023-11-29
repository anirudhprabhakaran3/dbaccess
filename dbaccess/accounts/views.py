from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.forms import RegisterForm


# Create your views here.

@login_required
def home(request):
    if request.user:
        if request.user.is_superuser:
            return redirect("admin_console_home")
        elif request.user.is_authenticated:
            return redirect("management_console_home")

@login_required
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_console_home")
    else:
        form = RegisterForm()
    args = {
        "form": form
    }
    return render(request, "accounts/register.html", args)
