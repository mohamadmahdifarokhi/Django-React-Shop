from django.test import TestCase
from .models import PercentageCoupon, FixedPriceCoupon


class CouponTestCase(TestCase):
    def setUp(self):
        PercentageCoupon.objects.create(
            name='percentage',
            discount_percentage=10
        )
        FixedPriceCoupon.objects.create(
            name='fixed',
            discount_price=10
        )

    def test_percentage_coupon(self):
        coupon = PercentageCoupon.objects.get(name='percentage')
        self.assertEqual(coupon.name, 'percentage')
        self.assertEqual(coupon.discount_percentage, 10)

    def test_fixed_price_coupon(self):
        coupon = FixedPriceCoupon.objects.get(name='fixed')
        self.assertEqual(coupon.name, 'fixed')
        self.assertEqual(coupon.discount_price, 10)

    def test_percentage_str(self):
        coupon = PercentageCoupon.objects.get(name='percentage')
        self.assertEqual(coupon.__str__(), 'percentage')

    def test_fixed_str(self):
        coupon = FixedPriceCoupon.objects.get(name='fixed')
        self.assertEqual(coupon.__str__(), 'fixed')
