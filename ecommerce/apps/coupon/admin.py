from django.contrib import admin
from .models import Coupon
from ..core.admin import BaseAdmin


@admin.register(Coupon)
class CouponAdmin(BaseAdmin):
    list_display = ['id', 'name', 'discount_price', 'discount_percentage', 'started', 'ended', 'created', 'last_updated',
                    'deleted_at', 'restored_at', 'is_deleted', 'is_active']
    list_filter = ['name']
    search_fields = ['name']
