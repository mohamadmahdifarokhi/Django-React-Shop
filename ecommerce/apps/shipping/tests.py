from django.test import TestCase
from .models import Shipping


class ShippingTestCase(TestCase):
    def setUp(self):
        Shipping.objects.create(name='Shipping 1', time='1-2 days', price=10.00, city='Tehran')

    def test_shipping(self):
        shipping1 = Shipping.objects.get(name='Shipping 1')
        self.assertEqual(shipping1.time, '1-2 days')
        self.assertEqual(shipping1.price, 10.00)
        self.assertEqual(shipping1.city, 'Tehran')
        self.assertNotEqual(shipping1.time, '2-3 days')
        self.assertNotEqual(shipping1.price, 20.00)
        self.assertNotEqual(shipping1.city, 'Mashhad')