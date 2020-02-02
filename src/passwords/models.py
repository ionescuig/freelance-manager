from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from projects.models import Project


class Password(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE)

    url        = models.URLField(blank=True, null=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

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
        elif self.url_github:
            return self.project.name + ' - ' + self.url_github
        elif self.url_digitalocean:
            return self.project.name + ' - ' + self.url_digitalocean
        elif self.url_other:
            return self.project.name + ' - ' + self.url_other
        else:
            return self.project.name + ' (not set)'

    def clean(self):
        if self.url and not self.username:
            raise ValidationError({'username': 'Please fill in this field.'})
        if self.url and not self.password:
            raise ValidationError({'password': 'Please fill in this field.'})

        if self.url_github and not self.username_github:
            raise ValidationError({'username_github': 'Please fill in this field.'})
        if self.url_github and not self.password_github:
            raise ValidationError({'password_github': 'Please fill in this field.'})

        if self.url_heroku and not self.username_heroku:
            raise ValidationError({'username_heroku': 'Please fill in this field.'})
        if self.url_heroku and not self.password_heroku:
            raise ValidationError({'password_heroku': 'Please fill in this field.'})

        if self.url_digitalocean and not self.username_digitalocean:
            raise ValidationError({'username_digitalocean': 'Please fill in this field.'})
        if self.url_digitalocean and not self.password_digitalocean:
            raise ValidationError({'password_digitalocean': 'Please fill in this field.'})

        if self.url_other and not self.username_other:
            raise ValidationError({'username_other': 'Please fill in this field.'})
        if self.url_other and not self.password_other:
            raise ValidationError({'password_other': 'Please fill in this field.'})

        if not self.url and not self.url_github and not self.url_heroku \
                and not self.url_digitalocean and not self.url_other:
            raise ValidationError('Please fill in at least one website.')

    def get_absolute_url(self):
        return reverse('passwords:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['project', 'url', 'url_github', 'url_heroku']
