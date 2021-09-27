from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(default="Default Summary !!!")
    """ blank is how field is rendered in admin null is for database"""
    featured = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return f"Product: {self.title}"

    def get_absolute_url(self):
        return reverse("products:prd_lookup", kwargs={"pid": self.id})
        # return f"/products/product/{self.id}/"
