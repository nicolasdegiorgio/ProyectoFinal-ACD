from django.shortcuts import render
from productos.forms import CargaProducto, FormularioBusqueda
from django.http import HttpResponse
from servicios.forms import CargaServicio
from servicios.models import Detailing

# Create your views here.
#Vista principal de servicios
def servicios (request):
    
    listado_servicios=Detailing.objects.all()
    
    return render (request, 'servicios/servicios.html', {'servicios': listado_servicios})

#Vista de carga de producto
def cargar_servicio(request):
    #El primer paso para crear el formulario de carga
    if request.method == "GET":
        formulario = CargaServicio()
        return render(request, 'servicios/crear_servicio.html', {"formulario": formulario})

    #se envia el formulario a través de POST
    else:

        formulario = CargaServicio(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
                  
            cliente = data.get("cliente")
            turno = data.get("turno")
            status = data.get('status')
            
            servicio = Detailing(cliente = cliente, turno = turno, status = status)

            servicio.save()

            return render(request, "productos/index.html")

        else:
            return HttpResponse("Formulario no valido")
        