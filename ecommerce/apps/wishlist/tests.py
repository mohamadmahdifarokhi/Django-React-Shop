from django.test import TestCase
from .models import WishList, WishListItem
from ..user.models import UserAccount


class WishListTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )
        WishList.objects.create(user=user, total_items=0)

    def test_wishlist(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        wishlist = WishList.objects.get(user=user)
        self.assertEqual(wishlist.total_items, 0)


