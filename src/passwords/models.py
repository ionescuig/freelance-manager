from django import forms
from django.db import models


class Password(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
