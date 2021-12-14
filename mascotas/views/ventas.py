from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.views.generic import ListView, DetailView
from django.views.generic.base import View 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models import Ventas,Productos,Servicios,Detalles
from django.db import transaction

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from django.urls import reverse

from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 

from django import forms

class VentasListado(ListView): 
    model = Ventas

class VentaDetalle(DetailView): 
    model = Ventas

class VentaCrear(SuccessMessageMixin, CreateView): 
    model = Ventas
    form = Ventas
    fields = "__all__" 
    success_message = 'Venta Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Venta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)
    
    def post(self, request):
        print(request.POST.get('cliente'))
        data = {
            "name": "Vaibhav",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
        }
        return JsonResponse(data)
        # return HttpResponse('some message')

    # Redireccionamos a la página principal luego de crear un registro o Venta
    def get_success_url(self):
        print(self)   
        return reverse('leer_ventas') # Redireccionamos a la vista principal 'ventas' 

class VentaActualizar(SuccessMessageMixin, UpdateView): 
    model = Ventas
    form = Ventas
    fields = "__all__"  
    success_message = 'Venta Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Venta 

    # Redireccionamos a la página principal luego de actualizar un registro o Venta
    def get_success_url(self):               
        return reverse('leer_ventas') # Redireccionamos a la vista principal 'ventas' 

class VentaEliminar(SuccessMessageMixin, DeleteView): 
    model = Ventas 
    form = Ventas
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Venta
    def get_success_url(self): 
        success_message = 'Venta Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Venta 
        messages.success (self.request, (success_message))       
        return reverse('leer_ventas') # Redireccionamos a la vista principal 'ventas'

@transaction.non_atomic_requests
class VentasGuardar(View):
    
    def post(self, request):
        body=json.loads(request.body)
        print(body)
        
        # Guardar la venta
        venta = Ventas(total=body['total'], cliente_id=body['cliente'])
        venta.save()

        # Actualizar stock de productos
        for producto in body['productos']:
            producto_obj = Productos.objects.get(id=producto['id'])
            producto_obj.stock = int(producto_obj.stock) - int(producto['cantidad'])
          
            producto_obj.save()

        # Guardar detalles de la venta
        for producto in body['productos']:
            detalle = Detalles(cantidad=producto['cantidad'], total=producto['total'], producto_id=producto['id'], venta_id=venta.id)
          
            detalle.save()

        for servicio in body['servicios']:
            detalle = Detalles(cantidad=servicio['cantidad'], total=servicio['total'], servicio_id=servicio['id'], venta_id=venta.id)
          
            detalle.save()
        
        data = {           
            "mensaje": "venta exitosa"
        }
        return JsonResponse(data)

class VentasExportar(View):
    
    def get(self, request):
        doc = SimpleDocTemplate("/tmp/ventas.pdf")
        styles = getSampleStyleSheet()
        Story = [Spacer(1,2*inch)]
        style = styles["Normal"]
        Story.append(Paragraph('REPORTE DE VENTAS', styles['title']))
        Story.append(Paragraph('', styles['title']))

        ventas = Ventas.objects.all()        

        for venta in ventas:
          print(venta.created_at)
          bogustext = ("Fecha:  "+str(venta.created_at)+ " Cliente:  "+venta.cliente.nombre + " Total:  "+str(venta.total)) 
          p = Paragraph(bogustext, style)
          Story.append(p)
          Story.append(Spacer(1,0.2*inch))

        doc.build(Story)

        fs = FileSystemStorage("/tmp")
        with fs.open("ventas.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="ventas.pdf"'
            return response