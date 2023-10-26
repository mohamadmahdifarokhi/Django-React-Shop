from django.test import TestCase
from .models import Review
from ..category.models import Category
from ..product.models import Product
from ..user.models import UserAccount


class ReviewTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )
        category = Category.objects.create(
            name='category'
        )
        product = Product.objects.create(
            name='product1',
            photo='photo1',
            description='description1',
            price=100,
            discount_price=200,
            category=category,
            count=1,
            sold=1,
        )

        Review.objects.create(
            user=user,
            product=product,
            rating=5,
            head='head',
            body='comment',
        )

    def test_review(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        product = Product.objects.get(name='product1')
        review = Review.objects.get(user=user, product=product)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.body, 'comment')
        self.assertEqual(review.head, 'head')
        self.assertNotEqual(review.body, 'comment1')
        self.assertNotEqual(review.head, 'head1')

    def test_str(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        product = Product.objects.get(name='product1')
        review = Review.objects.get(user=user, product=product)
        self.assertEqual(review.__str__(), 'head')



