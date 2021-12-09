from django.db import models
from django.utils import timezone

# Creación de campos de la tabla 'mascotas' 
class Mascotas(models.Model):
    SEXOS= (
      ('m','MACHO'),
      ('h', 'HEMBRA'),
    )
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=6, choices=SEXOS, default='m')
    img = models.FileField()
    amo = models.CharField(max_length=100)
    amo_telefono = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'mascotas' # Le doy de nombre 'mascotas' a nuestra tabla en la Base de Datos 

# Creación de campos de la tabla 'productos' 
class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=100)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'productos' # Le doy de nombre 'mascotas' a nuestra tabla en la Base de Datos 
