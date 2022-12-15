from django.contrib import admin
from .models import Review
from ..core.admin import BaseAdmin


@admin.register(Review)
class ReviewAdmin(BaseAdmin):
    list_display = ['user', 'product', 'head', 'body', 'rating', 'is_reply',
                    'reply', 'created', 'last_updated', 'deleted_at', 'restored_at', 'is_deleted', 'is_active']
    list_filter = ['user', 'product', 'is_reply']
    search_fields = ['user', 'product', 'head', 'body', 'rating', 'is_reply', 'reply']
