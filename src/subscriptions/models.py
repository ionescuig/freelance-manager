from datetime import date, timedelta
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from projects.models import Project
from websites.models import Website

User = get_user_model()


def date_renewal_default():
    return date.today()+timedelta(days=365)


class Subscription(models.Model):
    user         = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    project      = models.ForeignKey(Project, on_delete=models.CASCADE)
    website      = models.ForeignKey(Website, on_delete=models.CASCADE)

    date_created = models.DateField(blank=True, null=True)
    date_renewal = models.DateField(blank=True, null=True, default=date_renewal_default)
    notify_by_email = models.BooleanField(default=True)

    notes        = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.project.name + ' - ' + self.website.name

    def clean(self):
        if self.date_renewal:
            if self.date_renewal < date.today():
                raise ValidationError({"date_renewal": ValidationError("Renewal date cannot be in the past.")})
            if self.date_created:
                if self.date_renewal <= self.date_created:
                    raise ValidationError({"date_renewal": ValidationError("Renewal date must be after created date.")})

    def get_absolute_url(self):
        return reverse('subscriptions:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['project', 'website']
