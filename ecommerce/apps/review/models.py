from datetime import datetime

from apps.core.models import BaseModel
from apps.product.models import Product
from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class Review(BaseModel):
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, related_name='rcomments', blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    head = models.CharField(max_length=255)
    body = models.TextField(max_length=400)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.head
