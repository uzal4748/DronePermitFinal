from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=False)
    is_officer = models.BooleanField('Is officer', default=False)