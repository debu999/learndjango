from django.db import models


# Create your models here.
from oauth2.managers import OAuth2Manager


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tag = models.CharField(max_length=300, null=True)
    avatar = models.CharField(max_length=300, null=True)
    public_flags = models.IntegerField(null=True)
    flags = models.IntegerField(null=True)
    locale = models.CharField(max_length=300, null=True)
    mfa_enabled = models.BooleanField(null=True)
    last_login = models.DateTimeField(null=True)
    objects = OAuth2Manager()

    def is_authenticated(self, request):
        return True
