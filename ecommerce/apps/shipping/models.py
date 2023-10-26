from django.db import models

from apps.core.models import BaseModel
from apps.core.cities import Cities


class Shipping(BaseModel):
    class Meta:
        verbose_name = 'Shipping'
        verbose_name_plural = 'Shipping'

    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    city = models.CharField(
        max_length=255, choices=Cities.choices, default=Cities.Tehran)
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.name
