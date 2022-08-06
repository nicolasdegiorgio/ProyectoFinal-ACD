from django.urls import path
from clientes.views import *
urlpatterns = [
    path("crear/", crear_usuario),
    
]