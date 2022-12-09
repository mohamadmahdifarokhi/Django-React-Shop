from apps.core.models import BaseModel
from apps.product.models import Product
from django.db import models

from django.conf import settings
User = settings.AUTH_USER_MODEL


class WishList(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)


class WishListItem(BaseModel):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
