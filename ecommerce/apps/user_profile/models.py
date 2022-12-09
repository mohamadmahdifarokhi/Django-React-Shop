from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings

from apps.core.models import BaseModel

User = settings.AUTH_USER_MODEL
from apps.order.countries import Countries


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=255, default='')
    address_line_2 = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    state_province_region = models.CharField(max_length=255, default='')
    zipcode = models.CharField(max_length=20, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    country_region = models.CharField(
        max_length=255, choices=Countries.choices, default=Countries.Canada)

    def __str__(self):
        return self.phone
