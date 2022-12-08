from django.test import TestCase
from .models import UserProfile
from apps.user.models import UserAccount


class UserProfileTestCase(TestCase):
    def setUp(self):
        user = UserAccount.objects.create_user(
            email='mahdifarokhi@gmail.com',
            first_name='mahdi',
            last_name='farokhi',
            password='12345678Lte'
        )
        UserProfile.objects.create(
            user=user,
            address_line_1='address_line_1',
            address_line_2='address_line_2',
            city='city',
            state_province_region='state_province_region',
            zipcode='zipcode',
            phone='phone',
            country_region='country_region'
        )

    def test_user_profile(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(user_profile.address_line_1, 'address_line_1')
        self.assertEqual(user_profile.address_line_2, 'address_line_2')
        self.assertEqual(user_profile.city, 'city')
        self.assertEqual(user_profile.state_province_region, 'state_province_region')
        self.assertEqual(user_profile.zipcode, 'zipcode')
        self.assertEqual(user_profile.phone, 'phone')
        self.assertEqual(user_profile.country_region, 'country_region')

    def test_str(self):
        user = UserAccount.objects.get(
            email='mahdifarokhi@gmail.com'
        )
        user_profile = UserProfile.objects.get(user=user)
        self.assertEqual(user_profile.__str__(), user)
