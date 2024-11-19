from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
