from django.contrib import admin
from .models import cliente,factura,vehiculos,categoria_vehiculos

admin.site.register(cliente)
admin.site.register(factura)
admin.site.register(vehiculos)
admin.site.register(categoria_vehiculos)

def __str__(self):
    return (self.__all__)
