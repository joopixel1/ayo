# blog/admin.py
from django.contrib import admin
from .models import People, Service, Languages


admin.site.register(People)
admin.site.register(Service)
admin.site.register(Languages)
