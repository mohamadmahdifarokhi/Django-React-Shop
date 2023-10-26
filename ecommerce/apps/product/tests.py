from django.test import TestCase
from .models import Product
from ..category.models import Category


class ProductTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(
            name='category'
        )
        Product.objects.create(
            name='product1',
            photo='photo1',
            description='description1',
            price=100,
            discount_price=200,
            category=category,
            count=1,
            sold=1,
        )

    def test_product(self):
        category = Category.objects.get(name='category')
        product = Product.objects.get(name='product1')
        self.assertEqual(product.photo, 'photo1')
        self.assertEqual(product.description, 'description1')
        self.assertEqual(product.price, 100)
        self.assertEqual(product.discount_price, 200)
        self.assertEqual(product.category, category)
        self.assertEqual(product.count, 1)
        self.assertEqual(product.sold, 1)
        self.assertNotEqual(product.photo, 'photo2')
        self.assertNotEqual(product.description, 'description2')
        self.assertNotEqual(product.price, 200)

    def test_str(self):
        product = Product.objects.get(name='product1')
        self.assertEqual(product.__str__(), 'product1')
