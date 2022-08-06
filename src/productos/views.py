from django.shortcuts import render
from productos.forms import CargaProducto
from django.http import HttpResponse

from productos.models import ProductosDetailing

# Create your views here.
def index (request):
    
    listado_productos=ProductosDetailing.objects.all()
    
    return render (request, 'productos/index.html', {'productos': listado_productos})


def cargar_producto(request):

    if request.method == "GET":
        formulario = CargaProducto()
        return render(request, "productos/carga_productos.html", {"formulario": formulario})

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