from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView 
from django.views.generic.base import View 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Servicios

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

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

class ServicioBuscar(View): 

    def post(self, request):
        search = request.POST['search']
        queryset = Servicios.objects.filter(nombre__icontains=search).values()
        print(queryset) 
        data = {
            "name": "Vaibhav",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"],
            "servicios": list(queryset)
        }
        return JsonResponse(data)
    
    def get(self, request):
        print(request.GET)
        search = request.GET.get('search')
        print(search)
        queryset = Servicios.objects.filter(nombre__icontains=search).values()
        print(queryset) 
        data = {
            "name": "Vaibhav",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"],
            "servicios": list(queryset)
        }
        return JsonResponse(data)