from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from dbaccess.utils import is_user_authenticated

# Create your views here.
@user_passes_test(is_user_authenticated)
def home(request):
    return render(request, "management_console/home.html")