from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    username = None

    # login with email not username
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []
    
    def __str__(self):
        pass

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
