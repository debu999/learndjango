from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from oauth2.managers import OAuth2Manager


class User(AbstractUser):
    tag = models.CharField(max_length=300, null=True)
    avatar = models.CharField(max_length=300, null=True)
    public_flags = models.IntegerField(null=True)
    flags = models.IntegerField(null=True)
    locale = models.CharField(max_length=300, null=True)
    mfa_enabled = models.BooleanField(null=True)
    last_login = models.DateTimeField(null=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, unique=True, default="dummy@dummy.com")
    password = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, default="DUMMY_USER")
