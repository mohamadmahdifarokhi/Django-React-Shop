from django.test import TestCase
from .models import CartItem, Cart
from apps.user.models import UserAccount
from ..category.models import Category
from ..product.models import Product


class CartTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='regrh@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )

        cart = Cart.objects.create(
            user=user,
        )
        category = Category.objects.create(
            name='category',
        )
        product = Product.objects.create(
            name='product1',
            photo='photo1',
            description='description1',
            price=100,
            discount_price=200,
            category=category,
            quantity=1,
            sold=1,
        )

        CartItem.objects.create(
            cart=cart,
            product=product,
            count=3,
        )
