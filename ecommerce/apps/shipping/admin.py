from django.contrib import admin
from .models import Shipping
from ..core.admin import BaseAdmin


class ShippingAdmin(BaseAdmin):
    list_display = ('id', 'name', 'price',
                    'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_display_links = ('name',)
    list_editable = ('price',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Shipping, ShippingAdmin)
