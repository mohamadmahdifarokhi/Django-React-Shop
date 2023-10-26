from django.contrib import admin

from . import models

from django.contrib.auth import get_user_model

from ..core.admin import BaseAdmin

User = get_user_model()


class UserAdmin(BaseAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser',)
    list_display_links = ('email',)
    search_fields = ('email',)
    list_per_page = 25
    filter_horizontal = ['groups', 'user_permissions']

    fieldsets = [
        ['Main', {'fields': ['first_name', 'last_name', 'email', 'password']}],
        ['Permissions',
         # {'fields': ('is_active', ('is_superuser', 'is_staff', 'last_login'), 'groups', 'user_permissions')}],
         {'fields': ('is_active', 'is_superuser', 'is_staff', 'last_login', 'groups', 'user_permissions')}],
    ]

    add_fieldsets = [
        ['Main', {'fields': ['first_name', 'last_name', 'email', 'password']}],
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form


admin.site.register(User, UserAdmin)
