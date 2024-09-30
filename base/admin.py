from django.contrib import admin

# Register your models here.
from .models import Orders,Products

admin.site.register(Products)
admin.site.register(Orders)