# Generated by Django 3.1.3 on 2021-04-19 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_timesheet_is_booked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='is_booked',
        ),
    ]