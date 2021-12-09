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
from mascotas.views import MascotasListado, MascotaDetalle, MascotaCrear, MascotaActualizar, MascotaEliminar, ProductosListado, ProductoDetalle, ProductoCrear, ProductoActualizar, ProductoEliminar
#from . import views

#from mascotas.views import MascotasList

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # mascotas
    path('mascotas/', MascotasListado.as_view(template_name = "mascotas/index.html"), name='leer'),
    path('mascotas/detalle/<int:pk>', MascotaDetalle.as_view(template_name = "mascotas/detalles.html"), name='detalles'), 
    path('mascotas/crear', MascotaCrear.as_view(template_name = "mascotas/crear.html"), name='crear'),
    path('mascotas/editar/<int:pk>', MascotaActualizar.as_view(template_name = "mascotas/actualizar.html"), name='actualizar'),    
    path('mascotas/eliminar/<int:pk>', MascotaEliminar.as_view(), name='eliminar'), 

    #productos
    path('productos/', ProductosListado.as_view(template_name = "productos/index.html"), name='leer'), 
    path('productos/detalle/<int:pk>', ProductoDetalle.as_view(template_name = "productos/detalles.html"), name='detalles'),
    path('productos/crear', ProductoCrear.as_view(template_name = "productos/crear.html"), name='crear'),
    path('productos/editar/<int:pk>', ProductoActualizar.as_view(template_name = "productos/actualizar.html"), name='actualizar'), 
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
