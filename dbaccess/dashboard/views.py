from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect("admin_dashboard")
    else:
        return render(request, "dashboard/index.html")


@login_required
def admin(request):
    return render(request, "dashboard/admin.html")
