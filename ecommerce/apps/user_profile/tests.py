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

    # def test_user_profile(self):
    #     user = UserAccount.objects.get(
    #         email='mahdifarokhi@gmail.com',
    #     )

    #     user_profile = UserProfile.objects.get(user=user)
    #     self.assertEqual(user_profile.phone, '09123127203')
    #     self.assertEqual(user_profile.image, 'image')
    #     self.assertNotEqual(user_profile.phone, '091231272031')
    #     self.assertNotEqual(user_profile.image, 'image1')
    #     self.assertEqual(user_profile.address.body, 'onja')
    #     self.assertEqual(user_profile.address.city, 'tehran')

    # def test_str(self):
    #     user = UserAccount.objects.get(
    #         email='mahdifarokhi@gmail.com'
    #     )
    #     user_profile = UserProfile.objects.get(user=user)
    #     self.assertEqual(user_profile.__str__(), '09123127203')
