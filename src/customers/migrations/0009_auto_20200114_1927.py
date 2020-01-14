# Generated by Django 2.2.8 on 2020-01-14 19:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20200114_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='iban',
            field=models.CharField(blank=True, max_length=34, validators=[django.core.validators.RegexValidator(code='nomatch', message='Please use a valid phone number', regex='^[0-9A-Z]{15,32}$')]),
        ),
    ]
