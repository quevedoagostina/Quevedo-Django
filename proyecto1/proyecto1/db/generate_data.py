from django.core.management.base import BaseCommand
import random
from .models import Producto

class Command(BaseCommand):
    help = 'Genera datos aleatorios de productos y adjetivos'

    def handle(self, *args, **kwargs):
        nombres_productos = ["Laptop", "Teléfono", "Mouse", "Teclado", "Monitor", "Impresora"]
        adjetivos = ["Potente", "Elegante", "Rápido", "Compacto", "Eficiente", "Innovador"]

        for _ in range(400):  
            nombre_producto = random.choice(nombres_productos)
            adjetivo = random.choice(adjetivos)
            precio = round(random.uniform(100, 1000), 2)  

            producto = Producto.objects.create(nombre=f"{adjetivo} {nombre_producto}", precio=precio)

            self.stdout.write(self.style.SUCCESS(f"Producto creado: {producto}"))