from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from producto.views import ProductosIndex

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductosIndex.as_view()),
    path('productos/', include('producto.urls', namespace='producto')),
    path('pedidos/', include('pedido.urls', namespace='pedido')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
