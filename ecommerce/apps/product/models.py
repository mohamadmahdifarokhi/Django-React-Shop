from django.db import models
from datetime import datetime
from apps.category.models import Category

from django.conf import settings

from apps.core.models import BaseModel

domain = settings.DOMAIN


class Product(BaseModel):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    def get_thumbnail(self):
        if self.photo:
            return domain + self.photo.url

    def __str__(self):
        return self.name
