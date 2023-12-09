from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(AbstractUser):
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=50, default = make_password("password"))