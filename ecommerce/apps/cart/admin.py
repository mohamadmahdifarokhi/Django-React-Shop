from django.contrib import admin
from .models import Cart, CartItem


# admin.site.register(Cart)
# admin.site.register(CartItem)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_items', 'created', 'last_updated', 'deleted_at'
                    , 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_active', 'created', 'last_updated')
    search_fields = ('user',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'count', 'created', 'last_updated', 'deleted_at'
                    , 'restored_at', 'is_deleted', 'is_active')
    list_filter = ('is_active', 'created', 'last_updated')
    search_fields = ('cart', 'product')
