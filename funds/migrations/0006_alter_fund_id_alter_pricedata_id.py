# Generated by Django 4.0.6 on 2022-07-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0005_fund_category_fund_risk_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pricedata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
