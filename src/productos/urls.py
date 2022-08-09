from django.urls import path
from productos.views import *
urlpatterns = [
    path("", index, name= 'inicio'),
    path("cargarproducto/", cargar_producto, name= 'cargaproducto'),
    path('busqueda/', formulario_busqueda, name='buscar_producto'),
    path('resultados/', buscar, name='resultado_busqueda')
    
]