from django.contrib import admin

# Register your models here.

from . models import Alimento, Almacen, Medida
admin.site.register(Almacen)
admin.site.register(Alimento)
admin.site.register(Medida)
