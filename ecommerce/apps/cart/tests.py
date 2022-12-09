from django.test import TestCase
from .models import CartItem, Cart
from apps.user.models import UserAccount


class CartTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi1@gmail.com',
            first_name='mahdi1',
            last_name='farokhi1',
            password='12345678Ltee'
        )

        cart = Cart.objects.create(
            user=user,
            total_items=1,
        )

        CartItem.objects.create(
            cart=cart,
            user=user,
            count=1,
        )



