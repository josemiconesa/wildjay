from .views import ProductosIndex, ProductosVendidos, ProductosDisponibles
from django.urls import path

app_name = 'producto'

urlpatterns = [
    #path('detalles/<int:pk>/', ProductoDetalles.as_view(), name='productos-detalle'),
    path('index/', ProductosIndex.as_view(), name='productos-Index'),
    path('vendidos/', ProductosVendidos.as_view(), name='productos-vendidos'),
    path('disponibles/', ProductosDisponibles.as_view(), name='productos-disponibles'),
]