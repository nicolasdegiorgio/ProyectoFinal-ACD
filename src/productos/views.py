from django.shortcuts import render
from django.http import HttpResponse

#Forms 
from productos.forms import CargaProducto, FormularioBusqueda

#Decorators
from django.contrib.auth.decorators import login_required


#Models
from productos.models import ProductosDetailing
from clientes.models import Avatar


#Vista de inicio
def index (request):
    
    listado_productos=ProductosDetailing.objects.all()
    context = {
        'productos': listado_productos
    }
    
    if not request.user.is_anonymous:
        avatar = Avatar.objects.filter(usuario = request.user ).last()
        context.update({"avatar": avatar})
    
    return render (request, 'productos/index.html', context)

#Vista de carga de producto
@login_required
def cargar_producto(request):
    #El primer paso para crear el formulario de carga
    if request.method == "GET":
        formulario = CargaProducto()
        return render(request, "productos/carga_productos.html", {"formulario": formulario})

    #se envia el formulario a través de POST
    else:

        formulario = CargaProducto(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data
                  
            nombre = data.get("nombre")
            marca = data.get("marca")
            precio = data.get('precio')
            tipo = data.get('tipo')
            stock = data.get('stock')
            producto = ProductosDetailing(nombre = nombre, marca = marca, precio = precio, tipo = tipo, stock = stock)

            producto.save()

            return render(request, "productos/index.html")

        else:
            return HttpResponse("Formulario no valido")
        

#Formulario de busqueda, se utilizan los templates formulario_busqueda y resultado_busqueda
def formulario_busqueda(request):
    return render(request, "productos/formulario_busqueda.html")

def buscar(request):

    producto_nombre = request.GET.get("producto", None)
    

    if not producto_nombre:
        return HttpResponse("No indicaste ningun nombre")

    producto_lista = ProductosDetailing.objects.filter(nombre__icontains=producto_nombre)

        
    return render(request, "productos/resultado_busqueda.html", {"productos": producto_lista})
