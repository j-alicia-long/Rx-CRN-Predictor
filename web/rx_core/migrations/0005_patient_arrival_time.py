# Generated by Django 3.0.3 on 2020-04-19 13:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rx_core', '0004_auto_20200419_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='arrival_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]