from datetime import datetime

from django.test import TestCase
from .models import Coupon


class CouponTestCase(TestCase):
    def setUp(self):
        Coupon.objects.create(
            name='percentage',
            discount_percentage=10,
            started='2018-01-01 00:00:00',
            ended='2019-01-01 00:00:00',
        )

    def test_coupon(self):
        coupon = Coupon.objects.get(name='percentage')
        self.assertEqual(coupon.name, 'percentage')
        self.assertEqual(coupon.discount_percentage, 10)
        self.assertNotEqual(coupon.discount_price, 11)
        self.assertIsInstance(coupon.started, datetime)
        self.assertIsInstance(coupon.ended, datetime)

    def test_str(self):
        coupon = Coupon.objects.get(name='percentage')
        self.assertEqual(coupon.__str__(), 'percentage')
