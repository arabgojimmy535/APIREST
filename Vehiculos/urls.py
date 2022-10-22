from django.urls import path
from rest_framework import routers
from .api import clienteViewset, facturaViewset, vehiculosViewset, categoria_vehiculosViewset
app_name="Vehiculos"
router= routers.DefaultRouter()



router.register('api/clientes', clienteViewset , 'clientes')

router.register('api/factura', facturaViewset , 'facturas')

router.register('api/vehiculos', vehiculosViewset , 'vehiculos')

router.register('api/categoria_vehiculo', categoria_vehiculosViewset , 'categoria_vehiculo')



urlpatterns= router.urls