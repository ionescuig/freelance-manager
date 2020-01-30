from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.db import models

from passwords.models import Password
from projects.models import Project


websites = [
    ('123reg', '123Reg'),
    ('Heroku', 'Heroku'),
    ('GitHub', 'GitHub'),
    ('DigitalOcean', 'DigitalOcean'),
    ('Other', 'Other')
]


def date_renewal_default():
    return date.today()+timedelta(days=365)


class Subscription(models.Model):
    project      = models.ForeignKey(Project, on_delete=models.CASCADE)
    password     = models.OneToOneField(Password, on_delete=models.CASCADE)

    website      = models.CharField(choices=websites, default='GitHub', max_length=25)
    date_created = models.DateField(blank=True, null=True)
    date_renewal = models.DateField(blank=True, null=True, default=date_renewal_default)

    notes        = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.project.name + ' - ' + self.website

    def clean(self):
        if self.date_renewal:
            if self.date_renewal < date.today():
                raise ValidationError({"date_renewal": ValidationError("Renewal date cannot be in the past.")})
            if self.date_created:
                if self.date_renewal <= self.date_created:
                    raise ValidationError({"date_renewal": ValidationError("Renewal date must be after created date.")})
