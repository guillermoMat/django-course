from django.contrib import admin
from .models import Order,OrderProduct

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    model=Order

#le pasamos el modelo y la clase de configuración
admin.site.register(Order,OrderAdmin)
