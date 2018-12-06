from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('registro_venta', views.registroVenta, name='registro_venta'),
    path('productos_tienda', views.productosTienda, name='productos_tienda'),
    path('ofertas_tienda', views.ofertasTienda, name='ofertas_tienda'),
    path('ventas_realizadas', views.ventasRealizadas, name='ventas_realizadas'),
]