from django.db import models
from django.urls import reverse

from projects.models import Project
from websites.models import Website


class Password(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE)

    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)

    notes      = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.project.name + ' - ' + self.website.name

    def get_absolute_url(self):
        return reverse('passwords:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['project', 'website']
