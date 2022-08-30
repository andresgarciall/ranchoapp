from django.contrib import admin

from .models import Cliente, Servicios

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Servicios)