from django.db import models

from apps.core.models import BaseModel
from apps.product.models import Product
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Cart(BaseModel):
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class CartItem(BaseModel):
    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.cart}'
