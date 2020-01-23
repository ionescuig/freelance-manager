from django.db import models

from passwords.models import Password
from projects.models import Project


class Website(models.Model):
    project    = models.ForeignKey(Project, on_delete=models.CASCADE)
    password   = models.OneToOneField(Password, on_delete=models.CASCADE)

    url        = models.URLField(blank=True, null=True)
    url_github = models.URLField(blank=True, null=True)
    url_heroku = models.URLField(blank=True, null=True)

    notes      = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.url:
            return self.project.name + ' - ' + self.url
        elif self.url_heroku:
            return self.project.name + ' - ' + self.url_heroku
        else:
            return self.project.name + ' (not set)'
