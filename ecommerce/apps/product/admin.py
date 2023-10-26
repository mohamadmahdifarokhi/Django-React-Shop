from django.contrib import admin

from apps.core.admin import BaseAdmin
from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ('id', 'name', 'discount_price',
                    'price', 'sold', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_display_links = ('id',)
    list_filter = ('category',)
    list_editable = ('discount_price', 'price')
    search_fields = ('name', 'description',)
    list_per_page = 25
