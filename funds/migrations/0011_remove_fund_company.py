# Generated by Django 4.0.6 on 2022-07-28 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0010_remove_company_marketcap_alter_fund_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='company',
        ),
    ]
