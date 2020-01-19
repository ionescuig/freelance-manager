# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! No need to be added in admin !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from django.contrib import admin
from .models import Password


admin.site.register(Password)
