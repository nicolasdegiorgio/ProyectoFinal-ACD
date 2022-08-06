from django.urls import path
from clientes.views import *
urlpatterns = [
    path("crear/", crear_usuario, name='crearusuario'),
    path("clientes/", ver_clientes, name='clientes')
    
]