from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Mascotas, Clientes, Productos, Servicios

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

class Dashboard(ListView): 
    model = Mascotas

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['cantidad_mascotas'] = Mascotas.objects.count()
      context['cantidad_clientes'] = Clientes.objects.count()
      context['cantidad_productos'] = Productos.objects.count()
      context['cantidad_servicios'] = Servicios.objects.count()
      return context