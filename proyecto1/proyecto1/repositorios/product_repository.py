from proyecto1.db.models import(Producto, Categoria)
from typing import(List, Optional)


class ProductRepository:
    def create(self,
               name: str,
               price: float,
               stock: int,
               category: Optional[Categoria] = None,   
               description: Optional[str] = None,
               ) -> Producto.objects:
        return Producto.objects.create(
            categoria=category,
            nombre=name,
            precio=price,
            descripcion=description,
            stock=stock,
        )
        
    def get_all(self) -> List[Producto]:
        return Producto.objects.all()
    
    def get_by_id(self, product_id: int) -> Optional[Producto]:
        try:
            return Producto.objects.get(pk=product_id)
        except Producto.DoesNotExist:
            return None

    def get_by_price_range(self, min_price: float, max_price: float) -> List[Producto]:
        return Producto.objects.filter(precio__gte=min_price, precio__lte=max_price)