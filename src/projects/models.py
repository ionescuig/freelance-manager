from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from customers.models import Customer

User = get_user_model()


class Project(models.Model):
    user = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('projects:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['name', 'customer']
