# Generated by Django 3.1.3 on 2021-04-19 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20210227_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='is_booked',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
