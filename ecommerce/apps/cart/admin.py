from django.contrib import admin
from .models import Cart, CartItem
from ..core.admin import BaseAdmin


@admin.register(Cart)
class CartAdmin(BaseAdmin):
    list_display = ('user', 'total_items', 'created', 'last_updated', 'deleted_at'
                    , 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_active', 'created', 'last_updated')
    search_fields = ('user',)


@admin.register(CartItem)
class CartItemAdmin(BaseAdmin):
    list_display = ('cart', 'product', 'count', 'created', 'last_updated', 'deleted_at'
                    , 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_active', 'created', 'last_updated')
    search_fields = ('cart', 'product')
