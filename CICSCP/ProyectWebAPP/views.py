from django.shortcuts import render

def Home(request):
    return render(request, "ProyectWebAPP/Home.html")
# Create your views here.

def Servicios(request):
    return render(request, "ProyectWebAPP/Servicios.html")

def Tienda(request):
    return render(request, "ProyectWebAPP/Tienda.html")

def Precios(request):
    return render(request, "ProyectWebAPP/Precios.html")

def Contacto(request):
    return render(request, "ProyectWebAPP/Contacto.html")
