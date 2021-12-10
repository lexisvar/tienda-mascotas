from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mascotas, Productos, Servicios, Clientes

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

############ MASCOTAS #############

class MascotasListado(ListView): 
    model = Mascotas

class MascotaDetalle(DetailView): 
    model = Mascotas

class MascotaCrear(SuccessMessageMixin, CreateView): 
    model = Mascotas
    form = Mascotas
    fields = "__all__" 
    success_message = 'Mascota Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Mascota     

    # Redireccionamos a la página principal luego de crear un registro o mascota
    def get_success_url(self):        
        return reverse('leer_mascotas') # Redireccionamos a la vista principal 'mascotas' 

class MascotaActualizar(SuccessMessageMixin, UpdateView): 
    model = Mascotas
    form = Mascotas
    fields = "__all__"  
    success_message = 'Mascota Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Mascota 

    # Redireccionamos a la página principal luego de actualizar un registro o mascota
    def get_success_url(self):               
        return reverse('leer_mascotas') # Redireccionamos a la vista principal 'mascotas' 

class MascotaEliminar(SuccessMessageMixin, DeleteView): 
    model = Mascotas 
    form = Mascotas
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o mascota
    def get_success_url(self): 
        success_message = 'Mascota Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Mascota 
        messages.success (self.request, (success_message))       
        return reverse('leer_mascotas') # Redireccionamos a la vista principal 'mascotas'



############ PRODUCTOS #############

class ProductosListado(ListView): 
    model = Productos

class ProductoDetalle(DetailView): 
    model = Productos

class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = Productos
    form = Productos
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Producto     

    # Redireccionamos a la página principal luego de crear un registro o Producto
    def get_success_url(self):        
        return reverse('leer_productos') # Redireccionamos a la vista principal 'productos' 

class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Productos
    form = Productos
    fields = "__all__"  
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 

    # Redireccionamos a la página principal luego de actualizar un registro o Producto
    def get_success_url(self):               
        return reverse('leer_productos') # Redireccionamos a la vista principal 'productos' 

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Productos 
    form = Productos
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
        messages.success (self.request, (success_message))       
        return reverse('leer_productos') # Redireccionamos a la vista principal 'productos'


############ SERVICIOS #############

class ServiciosListado(ListView): 
    model = Servicios

class ServicioDetalle(DetailView): 
    model = Servicios

class ServicioCrear(SuccessMessageMixin, CreateView): 
    model = Servicios
    form = Servicios
    fields = "__all__" 
    success_message = 'Servicio Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Servicio     

    # Redireccionamos a la página principal luego de crear un registro o Servicio
    def get_success_url(self):        
        return reverse('leer_servicios') # Redireccionamos a la vista principal 'servicios' 

class ServicioActualizar(SuccessMessageMixin, UpdateView): 
    model = Servicios
    form = Servicios
    fields = "__all__"  
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Servicio 

    # Redireccionamos a la página principal luego de actualizar un registro o Servicio
    def get_success_url(self):               
        return reverse('leer_servicios') # Redireccionamos a la vista principal 'servicios' 

class ServicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Servicios 
    form = Servicios
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Servicio
    def get_success_url(self): 
        success_message = 'Servicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Servicio 
        messages.success (self.request, (success_message))       
        return reverse('leer_servicios') # Redireccionamos a la vista principal 'servicios'

############ CLIENTES #############

class ClientesListado(ListView): 
    model = Clientes

class ClienteDetalle(DetailView): 
    model = Clientes

class ClienteCrear(SuccessMessageMixin, CreateView): 
    model = Clientes
    form = Clientes
    fields = "__all__" 
    success_message = 'Cliente Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Cliente     

    # Redireccionamos a la página principal luego de crear un registro o Cliente
    def get_success_url(self):        
        return reverse('leer_clientes') # Redireccionamos a la vista principal 'clientes' 

class ClienteActualizar(SuccessMessageMixin, UpdateView): 
    model = Clientes
    form = Clientes
    fields = "__all__"  
    success_message = 'Cliente Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 

    # Redireccionamos a la página principal luego de actualizar un registro o Cliente
    def get_success_url(self):               
        return reverse('leer_clientes') # Redireccionamos a la vista principal 'clientes' 

class ClienteEliminar(SuccessMessageMixin, DeleteView): 
    model = Clientes 
    form = Clientes
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Cliente
    def get_success_url(self): 
        success_message = 'Cliente Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Cliente 
        messages.success (self.request, (success_message))       
        return reverse('leer_clientes') # Redireccionamos a la vista principal 'clientes'