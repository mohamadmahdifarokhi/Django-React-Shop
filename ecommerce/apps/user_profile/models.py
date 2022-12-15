from django.core.validators import RegexValidator
from django.db import models
from apps.core.models import BaseModel
from apps.core.cities import Cities
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Address(BaseModel):
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    body = models.TextField()
    city = models.CharField(
        max_length=255, choices=Cities.choices, default=Cities.Tehran)

    def __str__(self):
        return self.body


class UserProfile(BaseModel):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='address', blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True, default='profile_images/default.png')

    def __str__(self):
        return self.phone
