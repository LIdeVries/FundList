# Generated by Django 4.0.6 on 2022-07-28 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0005_alter_pricedata_marketcap_alter_pricedata_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
