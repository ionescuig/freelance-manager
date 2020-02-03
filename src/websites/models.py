from django.db import models
from django.urls import reverse


class Website(models.Model):
    name         = models.CharField(max_length=25, unique=True)
    url         = models.URLField(unique=True)
    subscription = models.BooleanField(default=True, blank=True, null=True)
    password     = models.BooleanField(default=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('websites:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['name']
