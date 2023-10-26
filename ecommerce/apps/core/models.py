from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from .managers import BaseManager


class BaseModel(models.Model):
    class Meta:
        abstract = True

    objects = BaseManager()

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
    )

    restored_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
    )

    is_deleted = models.BooleanField(
        default=False,
        editable=False,
        db_index=True,
    )

    is_active = models.BooleanField(
        default=True,
        editable=False,
    )

    def deleter(self, using=None):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save(using=using)

    def restore(self):
        self.restored_at = timezone.now()
        self.is_deleted = False
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()
