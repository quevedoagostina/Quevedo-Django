from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings
from django.utils.html import format_html

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Usuario(AbstractUser):
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1, null=True) 
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    def rango_precio(self):
        if self.precio < 1000:
            return 'Rango precio bajo'
        elif 1000 <= self.precio < 5000:
            return 'Rango precio medio'
        else:
            return 'Rango precio alto'

    def get_total(self):
        return self.precio * self.stock

class Adjetivo(models.Model):
    adjetivo = models.CharField(max_length=50)

    def __str__(self):
        return self.adjetivo

class Publicacion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='publicaciones_usuario')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
class Carrito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoItem')

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class Review(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='reviews')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField()
    puntuacion = models.PositiveIntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review de {self.usuario} para {self.producto}'

class Respuesta(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='respuestas')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Respuesta de {self.usuario} a la review de {self.review}'
