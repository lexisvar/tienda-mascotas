from django.contrib import admin

# Register your models here.
from .models import Mascotas, Productos, Servicios, Clientes
admin.site.register(Mascotas)
admin.site.register(Productos)
admin.site.register(Servicios)
admin.site.register(Clientes)