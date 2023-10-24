from django.shortcuts import render
from django.http import HttpResponse
from .models import Juego

# Create your views here.


def inicio(request):
    return render(request, "paginas/inicio.html")


def nosotros(request):
    return render(request, "paginas/nosotros.html")


def juegos(request):
    juegos = Juego.objects.all()
    return render(request, "juegos/index.html", {"juegos": juegos})


def crear(request):
    return render(request, "juegos/crear.html")


def editar(request):
    return render(request, "juegos/editar.html")
