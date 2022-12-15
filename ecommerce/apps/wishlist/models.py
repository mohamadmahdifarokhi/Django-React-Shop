from apps.core.models import BaseModel
from apps.product.models import Product
from django.db import models

from django.conf import settings

User = settings.AUTH_USER_MODEL


class WishList(BaseModel):
    class Meta:
        verbose_name = 'WishList'
        verbose_name_plural = 'WishLists'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class WishListItem(BaseModel):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
