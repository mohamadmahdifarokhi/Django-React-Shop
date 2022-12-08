from django.test import TestCase
from .models import Shipping


class ShippingTestCase(TestCase):
    def setUp(self):
        Shipping.objects.create(name='Shipping 1', time_to_delivery='1-2 days', price=10.00)
        Shipping.objects.create(name='Shipping 2', time_to_delivery='2-3 days', price=20.00)

    def test_shipping(self):
        shipping1 = Shipping.objects.get(name='Shipping 1')
        shipping2 = Shipping.objects.get(name='Shipping 2')
        self.assertEqual(shipping1.time_to_delivery, '1-2 days')
        self.assertEqual(shipping2.time_to_delivery, '2-3 days')