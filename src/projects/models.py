from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=35)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
