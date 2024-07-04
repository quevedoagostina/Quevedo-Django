from proyecto1.db.models import Categoria
from typing import List, Optional

class CategoryRepository:
    def create(self, name: str) -> Categoria:
        """Create a new category with the given name."""
        return Categoria.objects.create(nombre=name)
    
    def get_all(self) -> List[Categoria]:
        """Retrieve all categories."""
        return Categoria.objects.all()

    def get_by_id(self, category_id: int) -> Optional[Categoria]:
        """Retrieve a category by its ID, returning None if it does not exist."""
        try:
            return Categoria.objects.get(pk=category_id)
        except Categoria.DoesNotExist:
            return None

    def update(self, category_id: int, new_name: str) -> Optional[Categoria]:
        """Update the name of an existing category."""
        categoria = self.get_by_id(category_id)
        if categoria:
            categoria.nombre = new_name
            categoria.save()
            return categoria
        return None

    def delete(self, category_id: int) -> bool:
        """Delete a category by its ID, returning True if successful."""
        categoria = self.get_by_id(category_id)
        if categoria:
            categoria.delete()
            return True
        return False
