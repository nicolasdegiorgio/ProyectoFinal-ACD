from django.urls import path
from clientes.views import *


from django.contrib.auth.views import LogoutView
urlpatterns = [
    
    
    #sesiones
    path("registrate/", resgistrar_usuario, name = 'registro_usuario'),
    path("inicio_sesion/", iniciar_sesion, name='login'),
    path('profile/', datos_personales, name = 'datos_personales'),
    path('profile/modificar', modificar_usuario, name = 'modificar_usuario'),
    path('agregar_avatar/', agregar_avatar, name = 'agregar_avatar'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='productos/cerrar_sesion.html'), name='logout'),
    
    
    #footer
    path('about_me/', about_me, name='about_me'),
    path('contacto/', contacto, name='contacto'),
    
]