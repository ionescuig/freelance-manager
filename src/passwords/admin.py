# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! No need to be added in admin !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from django.contrib import admin
from .forms import PasswordForm
from .models import Password


class PasswordAdmin(admin.ModelAdmin):
    form = PasswordForm


admin.site.register(Password, PasswordAdmin)
