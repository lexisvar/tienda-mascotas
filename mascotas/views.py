from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mascotas, Productos

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

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
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class MascotaActualizar(SuccessMessageMixin, UpdateView): 
    model = Mascotas
    form = Mascotas
    fields = "__all__"  
    success_message = 'Mascota Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Mascota 

    # Redireccionamos a la página principal luego de actualizar un registro o mascota
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class MascotaEliminar(SuccessMessageMixin, DeleteView): 
    model = Mascotas 
    form = Mascotas
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o mascota
    def get_success_url(self): 
        success_message = 'Mascota Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Mascota 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'



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
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class ProductoActualizar(SuccessMessageMixin, UpdateView): 
    model = Productos
    form = Productos
    fields = "__all__"  
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 

    # Redireccionamos a la página principal luego de actualizar un registro o Producto
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer' 

class ProductoEliminar(SuccessMessageMixin, DeleteView): 
    model = Productos 
    form = Productos
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Producto
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Producto 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'