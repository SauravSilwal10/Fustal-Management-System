# Generated by Django 3.1.3 on 2021-04-20 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0008_auto_20210419_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('Pay on Site', 'Pay on Site'), ('Esewa', 'Esewa')], default='Pay on Site', max_length=20),
        ),
    ]
