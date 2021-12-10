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
         db_table = 'productos'

# Creación de campos de la tabla 'servicios' 
class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'servicios'

class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=10, unique=True)
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'clientes'

class ClientesMascotas(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'clientes_mascotas'

class Ventas(models.Model):
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, null=True)
    cantidad = models.IntegerField()
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         db_table = 'ventas'