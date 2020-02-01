# Generated by Django 2.2.9 on 2020-02-01 20:27

from django.db import migrations, models
import django.db.models.deletion
import subscriptions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(choices=[('123reg', '123Reg'), ('Heroku', 'Heroku'), ('GitHub', 'GitHub'), ('DigitalOcean', 'DigitalOcean'), ('Other', 'Other')], default='GitHub', max_length=25)),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=50)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_renewal', models.DateField(blank=True, default=subscriptions.models.date_renewal_default, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'ordering': ['project', 'website'],
            },
        ),
    ]
