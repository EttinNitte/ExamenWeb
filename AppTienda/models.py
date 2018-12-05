from django.db import models
from django.utils import timezone
# Create your models here.
class Vendedor(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)

class Venta(models.Model):
    vendedor = models.ForeignKey('AppTienda.Vendedor', on_delete=models.CASCADE)
    producto = models.ForeignKey('AppTienda.Producto', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.IntegerField()
    sucursal = models.ForeignKey('AppTienda.Sucursal', on_delete=models.CASCADE)
    comentario = models.TextField()

class Oferta(models.Model):
    producto = models.ForeignKey('AppTienda.Producto', on_delete=models.CASCADE)
    precio = models.IntegerField(max_length=10)
    descuento = models.IntegerField()

class Sucursal(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)

class Producto (models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    Sucursal = models.ManyToManyField('AppTienda.Sucursal')