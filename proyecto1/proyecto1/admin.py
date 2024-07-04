from django.contrib import admin
from django.utils.html import format_html
from .db.models import Categoria, Producto, Adjetivo, Publicacion, Review
from django.contrib.auth.admin import UserAdmin

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class StockFilter(admin.SimpleListFilter):
    title = 'Stock'
    parameter_name = 'stock'

    def lookups(self, request, model_admin):
        return (
            ('escaso', 'Escaso'),
            ('poco', 'Poco'),
            ('mucho', 'Mucho'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'escaso':
            return queryset.filter(stock__lt=50)
        elif self.value() == 'poco':
            return queryset.filter(stock__gte=50, stock__lt=100)
        elif self.value() == 'mucho':
            return queryset.filter(stock__gte=100)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'rango_precio', 'categoria', 'descripcion', 'stock_coloreado', 'get_total')  
    list_editable = ('precio',) 
    fieldsets = (
        (None, {
            'fields': ('nombre', 'precio')
        }),
        ('Información adicional', {
            'classes': ('collapse',),
            'fields': ('descripcion', 'stock')
        }),
    )
    list_filter = (StockFilter,)

    def rango_precio(self, obj):
        return obj.rango_precio()
    rango_precio.short_description = 'Rango de precios'  

    def stock_coloreado(self, obj):
        if obj.stock < 50:
            color = 'red'
            mensaje = 'Escaso'
        elif obj.stock < 100:
            color = 'orange'
            mensaje = 'Poco'
        else:
            color = 'green'
            mensaje = 'Mucho'
        return format_html('<span style="color:{};">{} ({})</span>', color, obj.stock, mensaje)
    stock_coloreado.short_description = 'Stock'

    def total(self, obj):
        return obj.get_total()
    total.short_description = 'Total'

@admin.register(Adjetivo)
class AdjetivoAdmin(admin.ModelAdmin):
    list_display = ('adjetivo',)

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'usuario', 'fecha_publicacion')
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('producto', 'usuario', 'puntuacion', 'fecha_creacion')