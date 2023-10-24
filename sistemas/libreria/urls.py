from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("juegos", views.juegos, name="juegos"),
    path("juegos/crear", views.crear, name="crear"),
    path("juegos/editar", views.editar, name="editar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
