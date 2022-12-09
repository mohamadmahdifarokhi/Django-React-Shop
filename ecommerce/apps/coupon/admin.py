from django.contrib import admin
from .models import FixedPriceCoupon, PercentageCoupon
from ..core.admin import BaseAdmin


class FixedPriceCouponAdmin(BaseAdmin):
    list_display = ('id', 'name', 'discount_price',)
    list_display_links = ('name',)
    list_editable = ('discount_price',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(FixedPriceCoupon, FixedPriceCouponAdmin)


class PercentageCouponAdmin(BaseAdmin):
    list_display = ('id', 'name', 'discount_percentage',)
    list_display_links = ('name',)
    list_editable = ('discount_percentage',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(PercentageCoupon, PercentageCouponAdmin)
