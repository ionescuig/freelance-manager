from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from projects.models import Project


class Website(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE)

    url        = models.URLField(blank=True, null=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)

    url_github      = models.URLField(blank=True, null=True)
    username_github = models.CharField(max_length=25, blank=True, null=True)
    password_github = models.CharField(max_length=50, blank=True, null=True)

    url_heroku      = models.URLField(blank=True, null=True)
    username_heroku = models.CharField(max_length=25, blank=True, null=True)
    password_heroku = models.CharField(max_length=50, blank=True, null=True)

    url_digitalocean      = models.URLField(blank=True, null=True)
    username_digitalocean = models.CharField(max_length=25, blank=True, null=True)
    password_digitalocean = models.CharField(max_length=50, blank=True, null=True)

    url_other      = models.URLField(blank=True, null=True)
    username_other = models.CharField(max_length=25, blank=True, null=True)
    password_other = models.CharField(max_length=50, blank=True, null=True)

    notes      = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.url:
            return self.project.name + ' - ' + self.url
        elif self.url_heroku:
            return self.project.name + ' - ' + self.url_heroku
        else:
            return self.project.name + ' (not set)'

    def clean(self):
        if self.url:
            self.username.__delattr__('blank')
            self.username.__delattr__('null')
            self.password.__delattr__('blank')
            self.password.__delattr__('null')

    def get_absolute_url(self):
        return reverse('websites:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['project', 'url', 'url_github', 'url_heroku']
