from django.contrib import admin

from apps.product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'compare_price',
                    'price', 'sold',)
    list_display_links = ('id', 'name',)
    list_filter = ('category',)
    list_editable = ('compare_price', 'price')
    search_fields = ('name', 'description',)
    list_per_page = 25
