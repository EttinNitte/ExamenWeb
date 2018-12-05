from django.http import HttpResponse
import requests
from django.shortcuts import render
from  . import models

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def registroVenta(request):
    return render(request,'registroVenta.html')
