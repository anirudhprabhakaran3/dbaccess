from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from console_user_management.models import (
    User,
    Role,
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
        fields = (
            "role_name",
            "role_description",
            "role_expiry",

            "console_user_management",
            "enterprise_meta_data_management",
            "enterprise_policy_management",
            "enterprise_data_product_management",
            "enterprise_role_config_management",
            "enterprise_policy_config_management",
            "enterprise_user_group_config_management",
            "enterprise_user_config_management",
        )
        widgets = {"role_expiry": forms.DateTimeInput(attrs={"type": "datetime-local"})}


class UserRoleAssignmentForm(forms.ModelForm):
    class Meta:
        model = UserRoleAssignment
        fields = ("user", "role", "expiry_date")

        widgets = {"expiry_date": forms.DateTimeInput(attrs={"type": "datetime-local"})}


class UserRoleMassUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserRoleMassUpdateForm, self).__init__(*args, **kwargs)
        self.initial['user'] = self.instance.user.email
        self.initial['role'] = self.instance.role.role_name

    class Meta:
        model = UserRoleAssignment
        fields = (
            "user",
            "role",
            "expiry_date"
        )

        widgets = {
            "user": forms.TextInput(attrs={"readonly": "readonly", "class": "form-control disabled"}),
            "role": forms.TextInput(attrs={"readonly": "readonly", "class": "form-control disabled"}),
            "expiry_date": forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"}),
        }


class UserSelectionForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())


class RoleSelectionForm(forms.Form):
    role = forms.ModelChoiceField(queryset=Role.objects.all())
