from django.shortcuts import render

from productos.models import ProductosDetailing

# Create your views here.
def index (request):
    
    
    
    return render (request, 'productos/index.html')