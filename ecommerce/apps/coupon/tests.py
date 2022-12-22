from datetime import datetime
import pytz
from django.test import TestCase
from .models import Coupon


class CouponTestCase(TestCase):
    def setUp(self):
        Coupon.objects.create(
            name='percentage',
            discount_percentage=10,
            started=datetime(2022, 11, 20, 20, 8, 7, 127325).replace(tzinfo=pytz.UTC),
            ended=datetime(2023, 12, 20, 20, 8, 7, 127325).replace(tzinfo=pytz.UTC),
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
