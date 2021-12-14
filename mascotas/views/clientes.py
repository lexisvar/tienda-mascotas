from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView
from django.views.generic.base import View 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.platypus.flowables import Spacer
from reportlab.lib.units import inch
from reportlab.platypus.paragraph import Paragraph
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

class ClienteBuscar(View): 
   
    def get(self, request):
        search = request.GET.get('search')
        queryset = Clientes.objects.filter(nombre__icontains=search).values()
        data = {          
            "clientes": list(queryset)
        }
        return JsonResponse(data)

class ClientesExportar(View):
    
    def get(self, request):
        doc = SimpleDocTemplate("/tmp/clientes.pdf")
        styles = getSampleStyleSheet()
        Story = [Spacer(1,2*inch)]
        style = styles["Normal"]
        Story.append(Paragraph('REPORTE DE Clientes', styles['title']))
        Story.append(Paragraph('', styles['title']))

        clientes = Clientes.objects.all()        

        for cliente in clientes:
          print(cliente.created_at)
          bogustext = ("Nombre:  "+str(cliente.nombre)+ " Identificación:  "+cliente.identificacion + " Teléfono:  "+str(cliente.telefono)) 
          p = Paragraph(bogustext, style)
          Story.append(p)
          Story.append(Spacer(1,0.2*inch))

        doc.build(Story)

        fs = FileSystemStorage("/tmp")
        with fs.open("clientes.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="clientes.pdf"'
            return response