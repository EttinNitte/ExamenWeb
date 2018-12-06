from django.contrib import admin
from .models import Vendedor,Venta,Tienda,Oferta,Producto

admin.site.register(Vendedor)
admin.site.register(Venta)
admin.site.register(Tienda)
admin.site.register(Oferta)
admin.site.register(Producto)