from django.test import TestCase

from .models import UserProfile, Address
from ..user.models import UserAccount


class UserProfileTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )
        address = Address.objects.create(
            body='onja',
            city='tehran',
        )
        UserProfile.objects.create(
            user=user,
            address=address,
            phone='wef',
            image='image',
        )
