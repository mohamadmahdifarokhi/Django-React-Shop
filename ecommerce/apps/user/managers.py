from django.contrib.auth.base_user import BaseUserManager

from apps.cart.models import Cart
from apps.user_profile.models import UserProfile
from apps.wishlist.models import WishList


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        shopping_cart = Cart.objects.create(user=user)
        shopping_cart.save()

        profile = UserProfile.objects.create(user=user)
        profile.save()

        wishlist = WishList.objects.create(user=user)
        wishlist.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
