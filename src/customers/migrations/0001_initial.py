# Generated by Django 2.2.9 on 2020-02-01 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='Please use a valid phone number', regex='^0\\d{10}$')])),
                ('town', models.CharField(default='Plymouth', max_length=20)),
                ('country', models.CharField(default='Great Britain', max_length=20)),
                ('company', models.CharField(blank=True, max_length=35)),
                ('address_first_line', models.CharField(blank=True, max_length=35)),
                ('post_code', models.CharField(blank=True, max_length=9)),
                ('sort_code', models.CharField(blank=True, max_length=6, validators=[django.core.validators.RegexValidator(code='nomatch', message='Invalid sort code', regex='^\\d{6}$')])),
                ('account_no', models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator(code='nomatch', message='Invalid account number. If the account number has less than 8 digits, please add 0(zero) in front.', regex='^\\d{8}$')])),
                ('iban', models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator(code='nomatch', message='Invalid IBAN. Please use CAPITAL LETTERS.', regex='^[0-9A-Z]{15,32}$')])),
                ('card_no', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(code='nomatch', message='Invalid card number', regex='^\\d{16}$')])),
                ('card_exp_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['company', 'name'],
            },
        ),
    ]
