# Generated by Django 4.0.6 on 2022-08-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0008_fund_one_month_fund_one_year_fund_six_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='pricing_data',
        ),
        migrations.AddField(
            model_name='fund',
            name='market_cap',
            field=models.FloatField(blank=True, default=999),
            preserve_default=False,
        ),
    ]
