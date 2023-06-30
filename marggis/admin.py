from django.contrib import admin
from .models import Genero, usuario, Producto, Contacto
# Register your models here.
class  ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    list_editable =["precio"]
    search_fields = ["nombre"]
    list_per_page = 8


admin.site.register(Genero)
admin.site.register(usuario)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)