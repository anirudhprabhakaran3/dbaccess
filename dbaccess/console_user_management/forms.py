from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from console_user_management.models import User, Role, RolePermissionAssignment


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name"
        )


class RoleCreationForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = (
            "role_name",
            "role_description",
            "role_expiry"
        )
        widgets = {
            "role_expiry": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }


class RolePermissionAssignmentForm(forms.ModelForm):
    class Meta:
        model = RolePermissionAssignment
        fields = (
            "permission",
            "permission_level",
        )

        widgets = {
            "permission": forms.TextInput(attrs={"readonly": "readonly"})
        }
