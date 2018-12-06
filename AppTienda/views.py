from django.http import HttpResponse
import requests
from django.shortcuts import redirect
from django.shortcuts import render
from  . import models
from .forms import VentaForm,LoginForm
from .models import Producto
from .models import Oferta
from .models import Venta
from .models import Vendedor

usuarioLogeado = 0

def index(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    global usuarioLogeado
    if usuarioLogeado == 0:
        return redirect('login')
    return render(request,'index.html',{'dolar': data['dolar']['valor'],'usuario': usuarioLogeado})
    
    
def productosTienda(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    global usuarioLogeado
    if usuarioLogeado == 0:
        return redirect('login')
    productos = Producto.objects.all().filter(Tienda=usuarioLogeado.Tienda)
    return render(request,'productosTienda.html',{'dolar': data['dolar']['valor'],'productos': productos,'usuario': usuarioLogeado})

def ofertasTienda(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    global usuarioLogeado
    if usuarioLogeado == 0:
        return redirect('login')
    ofertas = Oferta.objects.all().filter(Tienda=usuarioLogeado.Tienda)
    return render(request,'ofertasTienda.html',{'dolar': data['dolar']['valor'],'ofertas': ofertas,'usuario': usuarioLogeado})

def ventasRealizadas(request):
    response = requests.get('https://mindicador.cl/api')
    data = response.json()
    global usuarioLogeado
    if usuarioLogeado == 0:
        return redirect('login')
    ventas = Venta.objects.all().filter(vendedor = usuarioLogeado)
    total = 0
    for venta in ventas:
        total = total + (venta.producto.precio * venta.cantidad)
    return render(request,'ventasRealizadas.html',{'dolar': data['dolar']['valor'],'ventas': ventas,'usuario': usuarioLogeado,'total':total})

def login(request):
    response = requests.get('https://mindicador.cl/api')
    dataApi = response.json()
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print("FORMA VALIDA")
            data=form.cleaned_data
            usuarioValidado = Vendedor.objects.all().filter(usuario=data.get("usuario"),contraseña=data.get("contraseña"))
            if usuarioValidado.count() == 1:
                global usuarioLogeado
                usuarioLogeado = usuarioValidado.first()
                return redirect('index')
    else:
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
    return render(request, 'registroVenta.html', {'form': form,'dolar': data['dolar']['valor'],'usuario': usuarioLogeado})
