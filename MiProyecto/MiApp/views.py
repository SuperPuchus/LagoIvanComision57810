from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CategoriaForm, PublicacionForm, ComentarioForm, UsuarioPerfilForm
from .models import Categoria, Publicacion, Comentario, UsuarioPerfil
import logging

def home(request):
    return render(request, 'home.html')

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
    else:
        return redirect('home')

logger = logging.getLogger(__name__)

def custom_logout(request):
    logger.info('Logout request received.')
    logout(request)
    return redirect('/')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')
def buscar(request):
    query = request.GET.get('q')
    resultados = Publicacion.objects.filter(titulo__icontains=query)
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.autor = request.user
            publicacion.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = PublicacionForm()
    return render(request, 'crear_publicacion.html', {'form': form})

@login_required
def eliminar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('home')
    return render(request, 'MiApp/eliminar_publicacion.html', {'publicacion': publicacion})

def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_publicacion', pk=pk)
    else:
        form = ComentarioForm()
    return render(request, 'detalle_publicacion.html', {'publicacion': publicacion, 'form': form})

@login_required
def comentar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = ComentarioForm()
    return render(request, 'comentar_publicacion.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html')