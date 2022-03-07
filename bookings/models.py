from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.template.defaultfilters import date
# Create your models here.


class Arena(models.Model):
    arenaname = models.CharField(max_length=200)

    def __str__(self):
        return self.arenaname


class Timesheet(models.Model):
    times = models.CharField(max_length=200)

    def __str__(self):
        return self.times


class Date(models.Model):
    dates = models.DateField()
    arena = models.ManyToManyField(Arena, default=None, blank=True)
    timesheet = models.ManyToManyField(Timesheet, default=None, blank=True)

    def __str__(self):
        return str(self.dates)


class PaymentMethod(models.Model):
    payment_type = models.CharField(max_length=200, default=None, blank=True)

    def __str__(self):
        return str(self.payment_type)


class Booking(models.Model):
    date = models.ForeignKey(
        Date, default=None, on_delete=models.CASCADE, null=True, blank=True)
    payment_method = models.ForeignKey(
        PaymentMethod, default=None, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, null=True, blank=True)
    payment_completed = models.BooleanField(
        default=False, null=True, blank=True)

    # def __str__(self):
    #     user_details = self.user
    #     date_details = self.date
    #     arena = self.arena
    #     return "Booked by:  {} ".format(user_details) + " for {} " .format(date_details) + "at {} " .format(time) + "in {} " .format(arena)
