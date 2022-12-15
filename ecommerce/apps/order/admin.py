from django.contrib import admin
from .models import Order, OrderItem
from ..core.admin import BaseAdmin


class OrderAdmin(BaseAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('id', 'user', 'status',
                    'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_display_links = ('id',)
    list_filter = ('status',)
    list_editable = ('status',)
    list_per_page = 25


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(BaseAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('id', 'name', 'price',
                    'count', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_display_links = ('id',)
    list_per_page = 25


admin.site.register(OrderItem, OrderItemAdmin)
