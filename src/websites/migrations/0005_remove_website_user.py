# Generated by Django 2.2.9 on 2020-04-03 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0004_auto_20200403_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='user',
        ),
    ]
