# proyecto1/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistroForm, ProductoForm, ReviewForm, CategoriaForm, RespuestaForm
from .db.models import Producto, Carrito, CarritoItem, Review, Categoria
from .repositorios.category_repository import CategoryRepository  
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
import requests

def home(request):
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        exchange_rate = data.get('rates', {}).get('MXN', 20)
    except requests.exceptions.RequestException as e:
        exchange_rate = "Error obteniendo la tasa de cambio"
        print(f"Error: {e}")
    
    productos = Producto.objects.all()
    return render(request, 'home.html', {'exchange_rate': exchange_rate, 'productos': productos})

def lista_categorias(request):
    categorias = CategoryRepository().get_all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'editar_categoria.html', {'form': form})

def actualizar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'confirmar_eliminacion.html', {'categoria': categoria})

def detalle_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'detalle_categoria.html', {'categoria': categoria})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    reviews = Review.objects.filter(producto=producto).prefetch_related('respuestas')
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        respuesta_form = RespuestaForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.usuario = request.user
            review.producto = producto
            review.save()
            return redirect('detalle_producto', pk=producto.pk)
        elif respuesta_form.is_valid():
            respuesta = respuesta_form.save(commit=False)
            respuesta.usuario = request.user
            respuesta.review_id = request.POST.get('review_id')
            respuesta.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        review_form = ReviewForm()
        respuesta_form = RespuestaForm()
    return render(request, 'detalle_producto.html', {'producto': producto, 'review_form': review_form, 'respuesta_form': respuesta_form, 'reviews': reviews})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'confirmar_eliminacion.html', {'producto': producto})

def lista_productos(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    else:
        productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos, 'query': query})

def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, 'carrito.html', {'items': items})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'editar_producto.html', {'form': form})

def actualizar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def about(request):
    return render(request, 'about.html')
