from django.contrib import admin
from .models import Review
from ..core.admin import BaseAdmin


admin.site.register(Review, BaseAdmin)
