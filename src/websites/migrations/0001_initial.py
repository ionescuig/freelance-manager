# Generated by Django 2.2.9 on 2020-02-03 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('url', models.URLField(unique=True)),
                ('for_subscription', models.BooleanField(blank=True, default=True, null=True)),
                ('for_password', models.BooleanField(blank=True, default=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
