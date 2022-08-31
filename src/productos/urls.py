from django.urls import path
from productos.views import *
urlpatterns = [
    path("", index, name= 'inicio'),
    path('busqueda/', formulario_busqueda, name='buscar_producto'),
    path('resultados/', buscar, name='resultado_busqueda'),
    path('detalle/<int:pk>/', producto_detalle, name = 'productos_detalle'),
    
    
    #Generic
    path('todos/', ProductosList.as_view(), name = 'productos_lista'),
    path('cargar/', ProductosCrear.as_view(), name = 'productos_crear'),
    path('actualizar/<pk>', ProductosModificar.as_view(), name = 'productos_modificar'),
    path('borrar/<pk>', ProductosDelete.as_view(), name = 'productos_borrar'),
    
    
]