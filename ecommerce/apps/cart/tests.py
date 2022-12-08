from django.test import TestCase
from .models import Cart, CartItem
from apps.user.models import UserAccount
from ..product.models import Product


class CartTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )

        cart = Cart.objects.create(user=user, total_items=0)

    def test_cart(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        cart = Cart.objects.get(user=user)
        self.assertEqual(cart.total_items, 0)

