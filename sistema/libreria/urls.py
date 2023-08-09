from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("libros", views.libros, name="libros"),
    path("libros/crear", views.crear, name="crear"),
    path("libros/editar", views.editar, name="editar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
    path("libros/editar/<int:id>", views.editar, name="editar"),
    path("iniciar-sesion/", views.LoginPage, name="iniciar-sesion"),
    path("cerrar-sesion/", views.LogoutPage, name="cerrar-sesion"),
    path("registro", views.SignupPage, name="registro"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
