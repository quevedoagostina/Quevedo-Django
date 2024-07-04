"""
URL configuration for proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# proyecto1/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, about, registro, lista_productos, crear_producto, actualizar_producto, eliminar_producto, detalle_producto, signup, lista_categorias, crear_categoria, actualizar_categoria, eliminar_categoria, detalle_categoria, ver_carrito, agregar_al_carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('registro/', signup, name='registro'),  # Actualizado para usar la vista de registro
    path('productos/', lista_productos, name='lista_productos'),
    path('crear_producto/', crear_producto, name='crear_producto'),
    path('actualizar_producto/<int:pk>/', actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    path('detalle_producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),  
    path('signup/', signup, name='signup'), 
    path('categorias/', lista_categorias, name='lista_categorias'),
    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('actualizar_categoria/<int:pk>/', actualizar_categoria, name='actualizar_categoria'),
    path('eliminar_categoria/<int:pk>/', eliminar_categoria, name='eliminar_categoria'),
    path('detalle_categoria/<int:pk>/', detalle_categoria, name='detalle_categoria'),
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
]
