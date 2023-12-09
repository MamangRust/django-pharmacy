from django.db import models
from apps.user.models import User
from apps.products.models import Product
from apps.shared.models import TimeStampedModel

# Create your models here.


class Sale(TimeStampedModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name="sales"
    )
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Sale of {self.product} - Quantity: {self.quantity}, Total Price: {self.total_price}"
