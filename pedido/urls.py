from django.urls import path
from . import views

app_name = 'pedido'

urlpatterns = [
    path(r'', views.PedidosView, name='index'),
]