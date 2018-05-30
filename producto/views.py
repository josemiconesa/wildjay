from .models import Producto
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.views.generic import TemplateView

#class ProductoDetalles(DetailView):


class ProductosIndex(TemplateView):
    model = Producto
    template_name = 'producto/index.html'

    def dispatch(self, *args, **kwargs):
        return super(ProductosIndex, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductosIndex, self).get_context_data(**kwargs)
        productos = Producto.objects.all()
        context['productos'] = productos
        return context



class ProductosVendidos(TemplateView):
    model = Producto
    template_name = 'producto/vendidos.html'

    def dispatch(self, *args, **kwargs):
        return super(ProductosVendidos, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductosVendidos, self).get_context_data(**kwargs)
        productos = Producto.objects.filter(stock=0)
        context['productos'] = productos
        return context

class ProductosDisponibles(TemplateView):
    model = Producto
    template_name = 'producto/disponibles.html'

    def dispatch(self, *args, **kwargs):
        return super(ProductosDisponibles, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductosDisponibles, self).get_context_data(**kwargs)
        productos = Producto.objects.exclude(stock=0)
        context['productos'] = productos
        return context


