
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView
from django.views.generic.base import View 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Productos

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

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

class ProductoBuscar(View): 

    def post(self, request):
        search = request.POST['search']
        queryset = Productos.objects.filter(nombre__icontains=search).values()
        print(queryset) 
        data = {
            "name": "Vaibhav",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"],
            "productos": list(queryset)
        }
        return JsonResponse(data)
    
    def get(self, request):
        print(request.GET)
        search = request.GET.get('search')
        print(search)
        queryset = Productos.objects.filter(nombre__icontains=search).values()
        print(queryset) 
        data = {
            "name": "Vaibhav",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"],
            "productos": list(queryset)
        }
        return JsonResponse(data)