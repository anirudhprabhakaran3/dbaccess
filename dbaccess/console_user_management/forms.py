from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from console_user_management.models import (
    User,
    Role,
    RolePermissionAssignment,
    UserRoleAssignment,
)


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
    password = None

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class RoleCreationForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ("role_name", "role_description", "role_expiry")
        widgets = {"role_expiry": forms.DateTimeInput(attrs={"type": "datetime-local"})}


class RolePermissionAssignmentForm(forms.ModelForm):
    class Meta:
        model = RolePermissionAssignment
        fields = (
            "permission",
            "permission_level",
        )

        widgets = {"permission": forms.TextInput(attrs={"readonly": "readonly"})}


class UserRoleAssignmentForm(forms.ModelForm):
    class Meta:
        model = UserRoleAssignment
        fields = ("user", "role", "expiry_date")

        widgets = {"expiry_date": forms.DateTimeInput(attrs={"type": "datetime-local"})}


class UserSelectionForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())

class RoleSelectionForm(forms.Form):
    role = forms.ModelChoiceField(queryset=Role.objects.all())