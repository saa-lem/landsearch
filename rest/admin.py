from __future__ import unicode_literals
from django.contrib import admin

from .models import Property,Profile

# Register your models here.
admin.site.register(Property)
admin.site.register(Profile)