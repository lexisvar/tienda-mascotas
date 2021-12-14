"""tienda_mascotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from django.views.generic import TemplateView
from mascotas.views import MascotasListado, MascotaDetalle, MascotaCrear, MascotaActualizar, MascotaEliminar
from mascotas.views import ProductosListado, ProductoDetalle, ProductoCrear, ProductoActualizar, ProductoEliminar, ProductoBuscar
from mascotas.views import ServiciosListado, ServicioDetalle, ServicioCrear, ServicioActualizar, ServicioEliminar, ServicioBuscar
from mascotas.views import ClientesListado, ClienteDetalle, ClienteCrear, ClienteActualizar, ClienteEliminar, ClienteBuscar
from mascotas.views import VentasListado, VentaDetalle, VentaCrear, VentaActualizar, VentaEliminar, VentasGuardar
from mascotas.views import Dashboard
#from . import views

#from mascotas.views import MascotasList

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # mascotas
    path('', Dashboard.as_view(template_name = "dashboard/index.html"), name='dashboard'),
    path('dashboard/', Dashboard.as_view(template_name = "dashboard/index.html"), name='dashboard'),

    # mascotas
    path('mascotas/', MascotasListado.as_view(template_name = "mascotas/index.html"), name='leer_mascotas'),
    path('mascotas/detalle/<int:pk>', MascotaDetalle.as_view(template_name = "mascotas/detalles.html"), name='detalles_mascotas'), 
    path('mascotas/crear', MascotaCrear.as_view(template_name = "mascotas/crear.html"), name='crear_mascotas'),
    path('mascotas/editar/<int:pk>', MascotaActualizar.as_view(template_name = "mascotas/actualizar.html"), name='editar_mascotas'),    
    path('mascotas/eliminar/<int:pk>', MascotaEliminar.as_view(), name='eliminar_mascotas'), 

    #productos
    path('productos/', ProductosListado.as_view(template_name = "productos/index.html"), name='leer_productos'), 
    path('productos/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "productos/detalles.html"), name='detalles_productos'),
    path('productos/crear', ProductoCrear.as_view(template_name = "productos/crear.html"), name='crear_productos'),
    path('productos/editar/<int:pk>', ProductoActualizar.as_view(template_name = "productos/actualizar.html"), name='editar_productos'),
    path('productos/eliminar/<int:pk>', ProductoEliminar.as_view(), name='eliminar_productos'), 

    path('productos/buscar', ProductoBuscar.as_view(), name='buscar_productos'), 

    #servicios
    path('servicios/', ServiciosListado.as_view(template_name = "servicios/index.html"), name='leer_servicios'), 
    path('servicios/detalle/<int:pk>', ServicioDetalle.as_view(template_name = "servicios/detalles.html"), name='detalles_servicios'),
    path('servicios/crear', ServicioCrear.as_view(template_name = "servicios/crear.html"), name='crear_servicios'),
    path('servicios/editar/<int:pk>', ServicioActualizar.as_view(template_name = "servicios/actualizar.html"), name='editar_servicios'),
    path('servicios/eliminar/<int:pk>', ServicioEliminar.as_view(), name='eliminar_servicios'), 

    path('servicios/buscar', ServicioBuscar.as_view(), name='buscar_servicios'), 

    #clientes
    path('clientes/', ClientesListado.as_view(template_name = "clientes/index.html"), name='leer_clientes'), 
    path('clientes/detalle/<int:pk>', ClienteDetalle.as_view(template_name = "clientes/detalles.html"), name='detalles_clientes'),
    path('clientes/crear', ClienteCrear.as_view(template_name = "clientes/crear.html"), name='crear_clientes'),
    path('clientes/editar/<int:pk>', ClienteActualizar.as_view(template_name = "clientes/actualizar.html"), name='editar_clientes'),
    path('clientes/eliminar/<int:pk>', ClienteEliminar.as_view(), name='eliminar_clientes'), 

    path('clientes/buscar', ClienteBuscar.as_view(), name='buscar_clientes'), 

    #ventas
    path('ventas/', VentasListado.as_view(template_name = "ventas/index.html"), name='leer_ventas'), 
    path('ventas/detalle/<int:pk>', VentaDetalle.as_view(template_name = "ventas/detalles.html"), name='detalles_ventas'),
    path('ventas/crear', VentaCrear.as_view(template_name = "ventas/crear.html"), name='crear_ventas'),
    path('ventas/editar/<int:pk>', VentaActualizar.as_view(template_name = "ventas/actualizar.html"), name='editar_ventas'),
    path('ventas/eliminar/<int:pk>', VentaEliminar.as_view(), name='eliminar_ventas'), 

    path('ventas/guardar', VentasGuardar.as_view(), name='guardar_ventas'), 

] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
