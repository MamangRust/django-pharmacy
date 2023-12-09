from django.db import models
from apps.shared.models import TimeStampedModel


# Create your models here.
class Supplier(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    product = models.CharField(max_length=255, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
