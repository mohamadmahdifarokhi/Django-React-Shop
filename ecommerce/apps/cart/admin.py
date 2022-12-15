from django.contrib import admin
from .models import Cart, CartItem
from ..core.admin import BaseAdmin


admin.site.register(Cart, BaseAdmin)
admin.site.register(CartItem, BaseAdmin)