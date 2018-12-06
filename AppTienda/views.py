from django.http import HttpResponse
import requests
from django.shortcuts import redirect
from django.shortcuts import render
from  . import models
from .forms import VentaForm,LoginForm
from .models import Producto
from .models import Oferta
from .models import Venta

def index(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    return render(request,'index.html',{'dolar': data['dolar']['valor']})
    
    
def productosTienda(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    productos = Producto.objects.all()
    return render(request,'productosTienda.html',{'dolar': data['dolar']['valor'],'productos': productos})

def ofertasTienda(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    ofertas = Oferta.objects.all()
    return render(request,'ofertasTienda.html',{'dolar': data['dolar']['valor'],'ofertas': ofertas})

def ventasRealizadas(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    ventas = Venta.objects.all()
    return render(request,'ventasRealizadas.html',{'dolar': data['dolar']['valor'],'ventas': ventas})

def login(request):
    form = LoginForm()
    return render(request,'login.html', {'form': form})

def registroVenta(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    form = VentaForm()
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.save()
            return redirect('index')
    else:
        form = VentaForm()
    return render(request, 'registroVenta.html', {'form': form,'dolar': data['dolar']['valor']})
