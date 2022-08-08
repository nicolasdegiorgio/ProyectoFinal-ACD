from django.urls import path
from servicios.views import *
urlpatterns = [
    path("", servicios, name= 'inicio_servicios'),
    path("cargar/", cargar_servicio, name= 'carga_servicios'),
    
]