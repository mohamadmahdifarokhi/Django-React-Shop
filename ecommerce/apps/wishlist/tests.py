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
        WishList.objects.create(user=user)


