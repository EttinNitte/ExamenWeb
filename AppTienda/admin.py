from django.contrib import admin
from .models import Vendedor,Venta,Sucursal,Oferta

admin.site.register(Vendedor)
admin.site.register(Venta)
admin.site.register(Sucursal)
admin.site.register(Oferta)