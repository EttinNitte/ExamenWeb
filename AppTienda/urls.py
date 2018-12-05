from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registro_venta', views.registroVenta, name='registro_venta'),
]