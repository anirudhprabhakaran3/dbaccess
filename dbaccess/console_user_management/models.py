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


ROLE_PERMISSION_OPTIONS = [
    ("0", "None"),
    ("1", "View Reports"),
    ("2", "Create/Modify"),
    ("3", "Both")
]


class Role(models.Model):
    role_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    role_description = models.TextField(blank=True, null=True)
    role_expiry = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.role_name


class Permission(models.Model):
    permission_name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.permission_name


class RolePermissionAssignment(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    permission_level = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)

    def __str__(self):
        return f"{self.role} - {self.permission}"
