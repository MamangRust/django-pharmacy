from django.db import models
from apps.shared.models import TimeStampedModel
from apps.supplier.models import Supplier
from apps.category.models import Category


# Create your models here.
class Purchase(TimeStampedModel):
    product = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="purchases"
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, related_name="purchases"
    )
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.CharField(max_length=255)
    expiry_date = models.DateField(null=True)
    image = models.ImageField(upload_to="purchase_images/", null=True)

    def __str__(self):
        return self.product
