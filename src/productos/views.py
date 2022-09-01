
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse

#Generic views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#Forms 
from productos.forms import CommentForm

#Decorators
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#Models
from productos.models import ProductosDetailing, Comentarios
from clientes.models import Avatar


#Vista de inicio
@login_required
def base(request):
    usuario = request.user
    avatar = Avatar.objects.filter(usuario = usuario ).last()
    
    context = {
        'avatar': avatar
    }
    
    return render (request, 'productos/base.html', context)

def index (request):
    
    listado_productos=ProductosDetailing.objects.all()
    listado_productos_nuevo = []
    
    for i,producto in enumerate(listado_productos[::-1]):
        if i <= 1:
            listado_productos_nuevo.append(producto)
        
        
    avatar = Avatar.objects.filter(usuario = request.user ).last()
    
    context = {
        'productos': listado_productos_nuevo,
        'avatar':avatar
    }
       
    return render (request, 'productos/index.html', context)

        

#Formulario de busqueda, se utilizan los templates formulario_busqueda y resultado_busqueda
def formulario_busqueda(request):
    return render(request, "productos/formulario_busqueda.html")

def buscar(request):

    producto_nombre = request.GET.get("producto", None)
    

    if not producto_nombre:
        return HttpResponse("No indicaste ningun nombre")

    producto_lista = ProductosDetailing.objects.filter(nombre__icontains=producto_nombre)

        
    return render(request, "productos/resultado_busqueda.html", {"productos": producto_lista})



class ProductosList (ListView):
    model = ProductosDetailing
    template_name = 'productos/productos_lista.html'
    
    def get_context_data(self, **kwargs):
        context = super(ProductosList,self).get_context_data(**kwargs)
        context ['productos'] = ProductosDetailing.objects.all()
        return context


@login_required    
def producto_detalle(request, pk):

    producto = get_object_or_404(ProductosDetailing, pk=pk)
    comentarios = Comentarios.objects.filter(producto=producto)
    context = {
        'producto': producto
    }
    
    
    if request.method == 'GET':
        formulario = CommentForm()
        
        context ={
            'formulario':formulario,
            'comentarios' : comentarios,
            'producto': producto
        }
        return render (request, 'productos/productos_detalle.html', context)
    
    
    else:
        formulario = CommentForm(request.POST or None)
        
        if formulario.is_valid():
            contenido = request.POST.get('contenido')
            comentario = Comentarios.objects.create(producto = producto, usuario = request.user, contenido = contenido)
            comentario.save()
        return redirect('productos_lista')
           

class ProductosCrear (LoginRequiredMixin, CreateView):
    model = ProductosDetailing
    success_url = '../todos/'
    fields = ['nombre','marca','precio','tipo','stock', 'imagen','descripcion']
    template_name = 'productos/productos_crear.html'
    
    
class ProductosModificar (LoginRequiredMixin, UpdateView):
    model = ProductosDetailing
    success_url = '../todos/'
    fields = ['nombre','marca','precio','tipo','stock', 'imagen', 'descripcion']
    template_name = 'productos/productos_crear.html'
    
    
class ProductosDelete (LoginRequiredMixin, DeleteView):
    model = ProductosDetailing
    success_url = '../todos/'
    template_name = 'productos/confirmacion_borrado.html'
    
    
    
    
