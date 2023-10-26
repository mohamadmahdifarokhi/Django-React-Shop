from django.db import models

from apps.core.models import BaseModel


class Category(BaseModel):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name