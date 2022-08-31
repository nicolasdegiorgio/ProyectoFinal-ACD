from django.http import HttpResponse
from django.shortcuts import render, redirect
from clientes.forms import CrearUsuario
from clientes.models import Avatar

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

#Imports para registros y logeo de usuarios
from clientes.forms import UserCustomCreationForm, UserEditForm, AvatarForm


#Permisos usuarios
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.



    
    
def resgistrar_usuario(request):
    
    if request.method == 'GET':
        formulario = UserCustomCreationForm()
        context = {
            'formulario' : formulario
        }
        return render (request, 'clientes/authentication/registro.html', context)
    else:
        #obetiene la data del envio POST
        formulario = UserCustomCreationForm(request.POST)
        
        #verifica la validez del formulario
        if formulario.is_valid():
            formulario.save()
            return redirect ('inicio')
        else:
            context ={
                "formulario": formulario, 
                "error": "Formulario NO valido"
                }
            return render(request, "clientes/autentication/registro.html", context)
    
    
        
def iniciar_sesion (request):
    if request.method == 'GET':
        formulario = AuthenticationForm()
        
        context = {
            'formulario':formulario
        }
        
        return render (request, 'clientes/authentication/login.html', context)
    
    else:
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            usuario = authenticate(username=data.get('username'), password = data.get('password'))
            
            if usuario is not None:
                login(request, usuario)
                return redirect ('inicio')
            
            else:
                context = {
                    'error' : 'El usuario y/o la contraseña ingresados son incorrectos. Por favor ingreselos nuevamente', 
                    'formulario': formulario
                }
                return render (request, 'clientes/authentication/login.html', context)
            
        else:
            context = {
                'error': 'Formulario no valido',
                'formulario': formulario
            }
            return render (request, 'clientes/authentication/login.html', context)
        

@login_required
def datos_personales (request):
    usuario = request.user
    
    avatar = Avatar.objects.filter(usuario = request.user ).last()
    
    context = {
        'usuario': usuario,
        'avatar':avatar
    }
    
    return render (request, 'clientes/authentication/datos_personales.html', context)


@login_required
def modificar_usuario(request):
    
    if request.method == 'GET':
        
        formulario = UserEditForm(initial ={
            'email':request.user.email,
            'first_name': request.user.first_name,
            'last_name' : request.user.last_name
        })
        
        context = {
            'formulario' : formulario
        }
        return render(request, 'clientes/authentication/modificar_usuario.html', context)
    
    else:
        
        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            usuario = request.user

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("inicio")
        
        else:
            
            context = {
                'error': 'Formulario no valido',
                'formulario': formulario
            }
            
            return render(request, 'clientes/autentication/modificar_usuario.html', context )
        

@login_required
def agregar_avatar (request):
    
    if request.method == 'GET':
        formulario = AvatarForm()
        context ={
            'formulario':formulario
        }
        return render (request, 'clientes/authentication/agregar_avatar.html', context)
    
    else:
        formulario = AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            usuario = User.objects.filter(username=request.user.username).first()
            avatar = Avatar (usuario=usuario, imagen = data["imagen"])
            
            avatar.save()
            
            return redirect('inicio')
        
        
        context = {
            'formulario': formulario,
            'imagen': avatar
            }           
        
        return render(request, 'productos/index.html', context)
    
    
def about_me(request):
    return render (request, 'clientes/about_me.html')