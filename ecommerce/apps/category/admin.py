from django.contrib import admin
from .models import Category
from ..core.admin import BaseAdmin


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ('id', 'name', 'parent',
                    'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active')
    list_display_links = ('name', 'parent')
    search_fields = ('name', 'parent')
    list_per_page = 25
