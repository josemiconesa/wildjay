from django.shortcuts import render
from .models import Pedido
from django.http import HttpResponse

def PedidosView(request):
    if request.method == 'POST':
        pedido = Pedido()
        pedido.nombre = request.POST['nombre']
        pedido.email = request.POST['email']
        pedido.asunto = request.POST['asunto']
        pedido.mensaje = request.POST['mensaje']
        pedido.save()
        return HttpResponse('')

    return render(request, 'pedido/index.html', {})