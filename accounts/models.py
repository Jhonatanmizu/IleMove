import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    street = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=200, null=False, blank=False)
    state = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=False, blank=False)
    zip_code = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(
        "CustomUser", on_delete=models.CASCADE, null=True, blank=True
    )


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    user = models.OneToOneField("CustomUser", on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    identity_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
