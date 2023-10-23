from django.urls import path
from  . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('juegos', views.juegos, name='juegos'),
    path('juegos/crear', views.crear, name='crear'),
    path('juegos/editar', views.editar, name='editar'),
]
