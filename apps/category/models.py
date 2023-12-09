from django.db import models
from apps.shared.models import TimeStampedModel


# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
