from django import forms
from .models import Vendedor,Venta

class LoginForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Vendedor
        fields = ('usuario', 'contraseña',)

class VentaForm(forms.ModelForm):

    class Meta:    
        model = Venta 
        fields = ('vendedor','producto','fecha','cantidad','tienda','comentario',) 