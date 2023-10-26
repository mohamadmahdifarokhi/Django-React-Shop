from django.contrib import admin
from .models import WishList, WishListItem
from ..core.admin import BaseAdmin


@admin.register(WishList)
class WishListAdmin(BaseAdmin):
    list_display = ('user', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('user__email', 'user__phone_number')


@admin.register(WishListItem)
class WishListItemAdmin(BaseAdmin):
    list_display = (
        'wishlist', 'product', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('wishlist__user__email', 'wishlist__user__phone_number', 'product__name')
