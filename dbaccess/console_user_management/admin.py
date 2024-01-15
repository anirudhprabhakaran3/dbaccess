from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from console_user_management.forms import CustomUserCreationForm, CustomUserChangeForm
from console_user_management.models import User
from console_user_management.models import Role
from console_user_management.models import UserRoleAssignment


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)


class RoleAdmin(admin.ModelAdmin):
    search_fields = ("role_name", "role_description")
    list_display = (
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

class UserRoleAssignmentAdmin(admin.ModelAdmin):
    search_fields = ("user", "role")
    list_display = ("user", "role", "expiry_date")

admin.site.register(User, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(UserRoleAssignment, UserRoleAssignmentAdmin)
