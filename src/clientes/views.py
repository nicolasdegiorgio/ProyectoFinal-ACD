from django.http import HttpResponse
from django.shortcuts import render
from clientes.forms import CrearUsuario
from clientes.models import Usuarios
# Create your views here.


def crear_usuario(request):
    
    #Creamos la validacion del metodo para cargar el formulario
    if request.method == "GET":
        formulario = CrearUsuario()
        return render(request, 'clientes/formulario_usuario.html', {'formulario': formulario})
    
    
    #Una vez que se envia el formulario accedemos a los datos que van a través del POST
    #y creamos el dict con los datos
    else:
        
        formulario = CrearUsuario(request.POST)
                
        if formulario.is_valid():
            
            data = formulario.cleaned_data 
            
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            documento = data.get('documento')
            email = data.get('email')
                        
            usuario= Usuarios(nombre=nombre, apellido=apellido, documento= documento, email=email,)
            
            usuario.save()
            return render(request, 'productos/index.html')
        
        #Por ahora no es necesario
        else:
            return HttpResponse (f'usuario no valido')