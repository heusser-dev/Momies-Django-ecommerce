
# Register your models here.
# admin.py

from django.contrib import admin
from .models import Producto, Pedido, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio','stock','categoria']
    list_editable = ['precio']
    search_fields = ['nombre']
    list_per_page= 3

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Pedido)
admin.site.register(Categoria)
