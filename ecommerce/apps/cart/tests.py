from django.test import TestCase
from .models import CartItem, Cart
from apps.user.models import UserAccount


class CartTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
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

