from django.db import models
from apps.purchase.models import Purchase
from apps.shared.models import TimeStampedModel


# Create your models here.
class Product(TimeStampedModel):
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, null=True, related_name="products"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField(null=True)
