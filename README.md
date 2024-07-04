# Proyecto Django - Tienda Online

Este proyecto es una aplicación web de una tienda online creada con Django. Los usuarios pueden navegar por productos, leer y dejar reviews, y agregar productos a su carrito de compras.

## Características

- Autenticación de usuarios (registro y login)
- Listado de productos
- Detalle de productos con reviews y comentarios
- Carrito de compras
- Gestión de categorías y productos desde el panel de administración
- Sistema de reviews y respuestas a comentarios

## Requisitos

- Python 3.x
- Django 5.x
- Virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/quevedoagostina/Quevedo-Django.git
    cd Quevedo-Django
    ```

2. Crea y activa un entorno virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate  
    ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Configura la base de datos:

    ```sh
    python manage.py migrate
    ```

5. Carga datos de prueba (opcional):

    ```sh
    python manage.py loaddata initial_data.json
    ```

6. Ejecuta el servidor de desarrollo:

    ```sh
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador:

    ```
    http://127.0.0.1:8000
    ```

## Estructura del Proyecto

- `manage.py`: Script de administración de Django.
- `proyecto1/`: Directorio principal del proyecto.
  - `views.py`: Vistas de la aplicación.
  - `urls.py`: Configuración de rutas.
  - `settings.py`: Configuración del proyecto.
  - `forms.py`: Formularios de la aplicación.
  - `db/`: Modelos y generación de datos.
  - `repositorios/`: Repositorios para la gestión de datos.
  - `templates/`: Plantillas HTML.
