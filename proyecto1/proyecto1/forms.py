# forms.py

from django import forms
from .db.models import Usuario, Producto, Review, Respuesta
from django import forms
from .db.models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'direccion', 'telefono']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['categoria', 'nombre', 'precio', 'descripcion', 'stock']
        
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['producto', 'comentario', 'puntuacion']
        
class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['comentario']
