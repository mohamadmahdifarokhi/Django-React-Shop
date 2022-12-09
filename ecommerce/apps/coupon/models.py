from django.db import models

from apps.core.models import BaseModel


class FixedPriceCoupon(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PercentageCoupon(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    discount_percentage = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
