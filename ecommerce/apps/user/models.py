from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.user.managers import UserAccountManager


class UserAccount(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    # def has_perm(self, perm, obj=None):
    #     return True
    #
    # # karbar be modela datresi dare ya na
    # def has_module_perms(self, app_label):
    #     return True

    def __str__(self):
        return self.email
