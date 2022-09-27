from http.client import HTTPResponse
from django.shortcuts import render
from Articulos.models import Entrada
from django.http import HttpResponse

from Articulos.models import Entrada

# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "inicio.html",{"articulos":articulos})

def busqueda_articulos(request):
    return render(request,"busqueda_articulos.html")

def buscar(request):

    if request.GET["prd"]:

        #mensaje="Articulo buscado: %r"%request.GET["prd"]
        producto=request.GET["prd"]
        if len(producto)>20:

            mensaje="Lo ingeesado es demasiado largo"

        else:

           articulos=Entrada.objects.filter(autor__icontains=producto)

           return render(request, "resultado_busqueda.html",{"articulos":articulos, "query":producto})
        
    else:
         mensaje="no introdujiste nada"

    return HttpResponse(mensaje)

def contacto(request):
    if request.method=="POST":
        return render(request, "gracias.html")

    return render(request,"contacto.html")