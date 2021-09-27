from django.db import models

# Create your models here.
from django.db.models import Model
from django.urls import reverse


class Article(Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("articles:article_lookup", kwargs={"id": self.pk})
