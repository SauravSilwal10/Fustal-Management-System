# Generated by Django 3.1.3 on 2021-05-02 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0019_auto_20210501_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='new_list',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]