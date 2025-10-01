from django.contrib import admin

# Register your models here.

from . models import Alimento, Almacen
admin.site.register(Almacen)
admin.site.register(Alimento)
