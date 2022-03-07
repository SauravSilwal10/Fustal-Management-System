from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    captain_name = models.CharField(max_length=200, null=True, blank=True)
    no_of_members = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    logo = models.ImageField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
