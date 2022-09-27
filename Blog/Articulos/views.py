from django.shortcuts import render
from Articulos.models import Entrada

# Create your views here.
def home(request):
    articulos = Entrada.objects.all()
    return render(request, "inicio.html",{"articulos":articulos})