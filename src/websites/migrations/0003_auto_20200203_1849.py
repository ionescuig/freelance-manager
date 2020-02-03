# Generated by Django 2.2.9 on 2020-02-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0002_auto_20200203_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='link',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]