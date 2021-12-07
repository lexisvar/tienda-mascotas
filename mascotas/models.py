from django.db import models
from django.utils import timezone

# Creación de campos de la tabla 'mascotas' 
class Mascotas(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    stock = models.CharField(max_length=100)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'mascotas' # Le doy de nombre 'mascotas' a nuestra tabla en la Base de Datos 
