from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    temp = models.CharField(max_length=255, null=True, blank=True)

    REQUIRED_FIELDS = ['temp']  # Include any custom fields here
