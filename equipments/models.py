from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    user = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
