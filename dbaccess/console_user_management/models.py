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
]


class Role(models.Model):
    role_name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    role_description = models.TextField(blank=True, null=True)
    role_expiry = models.DateTimeField(blank=False, null=False)

    # Permissions
    console_user_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_meta_data_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_policy_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_data_product_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_role_config_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_policy_config_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_user_group_config_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)
    enterprise_user_config_management = models.CharField(max_length=1, choices=ROLE_PERMISSION_OPTIONS, blank=False, null=False)

    def __str__(self):
        return self.role_name

class UserRoleAssignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    expiry_date = models.DateTimeField(blank=False, null=False)

    class Meta:
        unique_together = ("user", "role")

    def __str__(self):
        return f"{self.user} - {self.role}"