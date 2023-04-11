from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUserModel

class CustomAdminModel(UserAdmin):
    list_display = ['username', 'email', 'last_login', 'is_staff']
    fieldsets = [
        ("Authentication", {"fields": ["username", "email", "password"]}),
        ("Personal Info", {"fields": ["full_name", "gender", "bio", "website_link", "display_email"]}),
        ("Permissons", {"fields": ["is_superuser", "is_staff", "is_active", "groups", "user_permissions"]}),
        ("Login Status", {"fields": ["date_joined", "last_login"]})
        ]
    search_fields = ['username', 'email']
    list_filter = ["is_superuser", "is_staff", "is_active"]
    ordering = ["username"]

admin.site.register(MyUserModel, CustomAdminModel)