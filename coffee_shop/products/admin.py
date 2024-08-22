from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model=Product

    #Elemento para mostrar los atributos que queramos en el admin
    list_display=["name","description","price","available","photo"]

    #Agregar un buscador para el admin, en este caso vamos a buscar por nombre
    #se puede poner otro atributo
    search_fields=["name"]

admin.site.register(Product,ProductAdmin)
