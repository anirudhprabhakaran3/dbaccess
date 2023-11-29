from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

from dbaccess.utils import is_user_superuser

# Create your views here.
@user_passes_test(is_user_superuser)
def home(request):
    users = User.objects.all()
    args = {
        "users": users,
    }
    return render(request, "admin_console/home.html", args)