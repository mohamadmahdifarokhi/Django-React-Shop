from django.contrib import admin
from .models import Cart, CartItem
from ..core.admin import BaseAdmin


@admin.register(Cart)
class CartAdmin(BaseAdmin):
    list_display = ['id', 'user', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active']
    list_filter = ['user']
    search_fields = ['user']


@admin.register(CartItem)
class CartItemAdmin(BaseAdmin):
    list_display = ['id', 'cart', 'product', 'count', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted',
                    'is_active']
    list_filter = ['cart', 'product', 'count']
    search_fields = ['cart', 'product', 'count']
