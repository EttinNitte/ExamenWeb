from django.db import models
from django.utils import timezone
# Create your models here.
class Vendedor(models.Model):
    usuario = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    Tienda = models.ForeignKey('AppTienda.Tienda', on_delete=models.CASCADE, default='1')
    
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    vendedor = models.ForeignKey('AppTienda.Vendedor', on_delete=models.CASCADE)
    producto = models.ForeignKey('AppTienda.Producto', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    cantidad = models.IntegerField()
    tienda = models.ForeignKey('AppTienda.Tienda', on_delete=models.CASCADE, default='1')
    comentario = models.TextField(blank=True, null=True)
    

class Oferta(models.Model):
    producto = models.ForeignKey('AppTienda.Producto', on_delete=models.CASCADE)
    precio = models.IntegerField(max_length=10)
    descuento = models.IntegerField()
    Tienda = models.ForeignKey('AppTienda.Tienda',blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.producto.nombre +' Oferta '+self.Tienda.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correoElectronico = models.CharField(max_length=100)
    encargado = models.ForeignKey('AppTienda.Vendedor', on_delete=models.CASCADE, blank=True, null=True, default=1)
    
    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    descripcion = models.TextField()
    tipo = models.CharField(max_length=200, default='a')
    Tienda = models.ManyToManyField('AppTienda.Tienda')

    def __str__(self):
        return self.nombre