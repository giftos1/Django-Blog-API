from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    name = models.EmailField(blank=True, null=True, max_length=100)

