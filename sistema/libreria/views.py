from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, "paginas/inicio.html")


def nosotros(request):
    return render(request, "paginas/nosotros.html")


@login_required(login_url="iniciar-sesion")
def libros(request):
    Libros = Libro.objects.all()
    return render(request, "libros/index.html", {"libros": Libros})


def crear(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("libros")
    return render(request, "libros/crear.html", {"formulario": formulario})


def editar(request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect("libros")
    return render(request, "libros/editar.html", {"formulario": formulario})


def eliminar(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect("libros")


def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("iniciar-sesion")

    return render(request, "autenticacion/registro.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("libros")
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, "autenticacion/iniciar-sesion.html")


def LogoutPage(request):
    logout(request)
    return redirect("iniciar-sesion")
