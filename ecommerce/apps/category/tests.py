from django.test import TestCase
from .models import Category


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(
            name='category'
        )

    def test_category(self):
        category = Category.objects.get(name='category')
        self.assertEqual(category.name, 'category')
        self.assertNotEqual(category.name, 'category1')

    def test_str(self):
        category = Category.objects.get(name='category')
        self.assertEqual(category.__str__(), 'category')
