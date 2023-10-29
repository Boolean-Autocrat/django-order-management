from django.db import models
from django.contrib.auth.models import User
import uuid


class Orders(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
