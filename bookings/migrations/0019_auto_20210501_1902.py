# Generated by Django 3.1.3 on 2021-05-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0018_auto_20210501_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='dates',
            field=models.DateField(),
        ),
    ]
