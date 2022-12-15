from django.contrib import admin

# Register your models here.
from .models import UserProfile, Address


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address',
                    'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('user__email', 'user__phone_number', 'phone')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('body', 'city', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('body', 'city')
