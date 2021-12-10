from django.contrib import admin

# Register your models here.
from .models import Mascotas, Productos, Servicios
admin.site.register(Mascotas)
admin.site.register(Productos)
admin.site.register(Servicios)