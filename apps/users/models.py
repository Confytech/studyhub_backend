from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Add only your custom fields here.
    DO NOT redefine groups or user_permissions.
    """

    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Added custom fields
    coins = models.IntegerField(default=0)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username

