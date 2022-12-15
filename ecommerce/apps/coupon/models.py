from django.db import models

from apps.core.models import BaseModel


class Coupon(BaseModel):
    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    name = models.CharField(max_length=255, unique=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    discount_percentage = models.IntegerField(blank=True, null=True)
    started = models.DateTimeField()
    ended = models.DateTimeField()

    def __str__(self):
        return self.name

