# Generated by Django 2.2.9 on 2020-04-03 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_website_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='websites', to=settings.AUTH_USER_MODEL),
        ),
    ]
