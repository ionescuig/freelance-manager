from django.db import models

from customers.models import Customer


class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
