from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Clientes

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

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