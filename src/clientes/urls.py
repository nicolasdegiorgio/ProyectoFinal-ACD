from django.urls import path
from clientes.views import *


from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("crear/", crear_usuario, name='crearusuario'),
    path("", ver_clientes, name='clientes'),
    
    #sesiones
    path("authentication/registrate/", resgistrar_usuario, name = 'registro_usuario'),
    path("authentication/inicio_sesion/", iniciar_sesion, name='login'),
    path('authentication/modificar_usuario/', modificar_usuario, name = 'modificar_usuario'),
    path('authentication/agregar_avatar/', agregar_avatar, name = 'agregar_avatar'),
    path('authentication/cerrar_sesion/', LogoutView.as_view(template_name='productos/index.html'), name='logout'),
    
    
]