from django.shortcuts import render

from productos.models import ProductosDetailing

# Create your views here.
def index (request):
    
    listado_productos = ProductosDetailing.objects.all()
    
    if request.GET.get('nombre_producto'):
        
        formulario = FormularioBusqueda(request.GET)
        
        if formulario.isvalid():
            data = formulario.cleaned_data
            listado_productos = listado_productos.filter(nombre__icontains = data('nombre_producto'))
            
            
        return render(request, 'productos/index.html', {'productos':listado_productos})

    
    else:
        formulario = FormularioBusqueda
        return render(request, 'productos/index.html', {'productos':listado_productos, 'formulario':formulario})
    
    return render (request, 'productos/index.html')