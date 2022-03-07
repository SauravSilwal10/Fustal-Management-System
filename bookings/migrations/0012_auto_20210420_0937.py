# Generated by Django 3.1.3 on 2021-04-20 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0011_auto_20210420_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='payment_method',
            field=models.CharField(choices=[('Pay on Site', 'Pay on Site'), ('Esewa', 'Esewa')], default='Pay on Site', max_length=20, verbose_name=''),
        ),
    ]