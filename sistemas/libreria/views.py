from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Juego
from .forms import JuegoForm

# Create your views here.


def inicio(request):
    return render(request, "paginas/inicio.html")


def nosotros(request):
    return render(request, "paginas/nosotros.html")


def juegos(request):
    juegos = Juego.objects.all()
    return render(request, "juegos/index.html", {"juegos": juegos})


def crear(request):
    formulario = JuegoForm(request.POST or None, request.FILES or None)
    return render(request, "juegos/crear.html", {"formulario": formulario})
    if formulario.is_valid():
        formulario.save()
    return redirect("juegos")
    return render(request, "juegos/crear.html", {"formulario": formulario})


def editar(request):
    juego = Juego.objects.get(id=id)
    formulario = JuegoForm(request.POST or None, request.FILES or None, instance=juego)
    return render(request, "juegos/editar.html", {"formulario": formulario})


def eliminar(request, id):
    juego = Juego.objects.get(id=id)
    juego.delete()
    return render(request, "juegos")
