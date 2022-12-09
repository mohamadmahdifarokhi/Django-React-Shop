from django.contrib import admin

from . import models

from django.contrib.auth import get_user_model

from ..core.admin import BaseAdmin

User = get_user_model()


class UserAdmin(BaseAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_display_links = ('first_name', 'last_name', 'email',)
    search_fields = ('first_name', 'last_name', 'email', 'is_staff', 'is_superuser', 'is_active', 'last_login')
    list_per_page = 25


admin.site.register(User, UserAdmin)
