from django.db import models
from django.core.validators import MinValueValidator
import os


class Almacen(models.Model):
    id_almacen = models.AutoField(primary_key=True)
    desc_almacen = models.CharField(max_length=400, default="?")
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.desc_almacen

    class Meta:
        db_table = 'almacenes'


def alimento_imagen_ruta(instance, filename):
    return f'alimentos/{instance.id_alimento}/{filename}'


class Alimento(models.Model):
    id_alimento = models.AutoField(primary_key=True)
    imagen_alimento = models.ImageField(upload_to=alimento_imagen_ruta, null=True, blank=True)
    desc_alimento = models.CharField(max_length=400, default="?")
    cantidad = models.DecimalField(default=0.0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    almacen_perteneciente = models.ForeignKey(Almacen, on_delete=models.SET_NULL, null=True, blank=True, related_name='alimentos')

    def __str__(self):
        return self.desc_alimento

    class Meta:
        db_table = 'alimentos'

    def delete(self, using=None, keep_parents=False):
        if self.imagen_alimento:
            if os.path.isfile(self.imagen_alimento.path):
                os.remove(self.imagen_alimento.path)
        super().delete(using=using, keep_parents=keep_parents)
