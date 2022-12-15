from django.test import TestCase
from .models import Order, OrderItem
from ..category.models import Category
from ..coupon.models import Coupon
from ..product.models import Product
from ..user.models import UserAccount


class OrderTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )
        coupon = Coupon.objects.create(
            name='percentage',
            discount_percentage=10,
            started='2018-01-01 00:00:00',
            ended='2019-01-01 00:00:00',
        )

        Order.objects.create(
            user=user,
            coupon=coupon,
            transaction_id='2',
            full_name='mahdi farokhi',
            address='onja',
            city='tehran',
            price=100,
            discount_price=10,
            shipping_name='shipping_name',
            shipping_price=10.00,
            shipping_time='3 days',
            status='processed'
        )
        category = Category.objects.create(
            name='category',
        )
        product = Product.objects.create(
            name='product1',
            photo='photo.jpg',
            description='description1',
            price=100,
            discount_price=200,
            category=category,
            count=1,
            sold=1,
        )

        OrderItem.objects.create(
            order=Order.objects.get(transaction_id='2'),
            product=product,
            name='product',
            price=100,
            discount_price=10,
            count=1,
            status='processed'
        )

    def test_order(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        order = Order.objects.get(user=user)
        self.assertEqual(order.user, user)
        self.assertEqual(order.coupon.name, 'percentage')
        self.assertEqual(order.transaction_id, '2')
        self.assertEqual(order.full_name, 'mahdi farokhi')
        self.assertEqual(order.address, 'onja')
        self.assertEqual(order.city, 'tehran')
        self.assertEqual(order.price, 100)
        self.assertEqual(order.discount_price, 10)
        self.assertEqual(order.shipping_name, 'shipping_name')
        self.assertEqual(order.shipping_price, 10.00)
        self.assertEqual(order.shipping_time, '3 days')
        self.assertEqual(order.status, 'processed')
        self.assertNotEqual(order.status, 'not_processed')
        self.assertNotEqual(order.coupon.name, 'not_percentage')

    def test_str(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        order = Order.objects.get(user=user)
        self.assertEqual(order.__str__(), '2')

    def test_order_item(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        order = Order.objects.get(user=user)
        order_item = OrderItem.objects.get(order=order)
        product = Product.objects.get(name='product1')
        self.assertEqual(order_item.order, order)
        self.assertEqual(order_item.product, product)
        self.assertEqual(order_item.name, 'product')
        self.assertEqual(order_item.price, 100)
        self.assertEqual(order_item.discount_price, 10)
        self.assertEqual(order_item.count, 1)
        self.assertEqual(order_item.status, 'processed')
        self.assertNotEqual(order_item.status, 'not_processed')
        self.assertNotEqual(order_item.name, 'not_product')

    def test_str(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        order = Order.objects.get(user=user)
        order_item = OrderItem.objects.get(order=order)
        self.assertEqual(order_item.__str__(), 'product')




