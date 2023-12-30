from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from console_user_management.managers import UserManager


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Role(models.Model):
    role_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    role_description = models.TextField(blank=True, null=True)
    role_expiry = models.DateTimeField(blank=False, null=False)
