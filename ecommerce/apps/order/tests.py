from django.test import TestCase
from .models import Order, OrderItem
from ..user.models import UserAccount


class OrderTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )
        Order.objects.create(
            status='processed',
            user=user,
            transaction_id='2',
            amount=100,
            full_name='mahdi farokhi',
            address_line_1='address_line_1',
            address_line_2='address_line_2',
            city='city',
            state_province_region='state_province_region',
            postal_zip_code='postal_zip_code',
            country_region='iran',
            telephone_number='telephone_number',
            shipping_name='shipping_name',
            shipping_time='shipping_time',
            shipping_price=10.00,
        )

    def test_order(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        order = Order.objects.get(user=user)
        self.assertEqual(order.status, 'processed')
        self.assertEqual(order.transaction_id, '2')
        self.assertEqual(order.amount, 100)
        self.assertEqual(order.full_name, 'mahdi farokhi')
        self.assertEqual(order.address_line_1, 'address_line_1')
        self.assertEqual(order.address_line_2, 'address_line_2')
        self.assertEqual(order.city, 'city')
        self.assertEqual(order.state_province_region, 'state_province_region')
        self.assertEqual(order.postal_zip_code, 'postal_zip_code')
        self.assertEqual(order.country_region, 'iran')
        self.assertEqual(order.telephone_number, 'telephone_number')
        self.assertEqual(order.shipping_name, 'shipping_name')
        self.assertEqual(order.shipping_time, 'shipping_time')
        self.assertEqual(order.shipping_price, 10.00)

    def test_str(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        order = Order.objects.get(user=user)
        self.assertEqual(order.__str__(), '2')
