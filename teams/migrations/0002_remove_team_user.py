# Generated by Django 3.1.3 on 2021-04-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='user',
        ),
    ]