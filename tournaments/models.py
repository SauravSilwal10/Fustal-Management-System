from django.db import models
from django.contrib.auth.models import User
from teams.models import Team
# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    prize = models.TextField(max_length=500, null=True, blank=True)
    banner = models.ImageField(null=True, blank=True)
    created_at = models.DateField()
    end_date = models.DateField()
    team = models.ManyToManyField(Team, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
