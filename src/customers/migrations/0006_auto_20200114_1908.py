# Generated by Django 2.2.8 on 2020-01-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20200114_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='obs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
