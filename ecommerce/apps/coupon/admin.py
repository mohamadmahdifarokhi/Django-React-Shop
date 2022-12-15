from django.contrib import admin
from .models import Coupon
from ..core.admin import BaseAdmin


admin.site.register(Coupon, BaseAdmin)