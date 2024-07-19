from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from .views import custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', custom_logout, name='logout'),
    path('crear-publicacion/', views.crear_publicacion, name='crear_publicacion'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('publicacion/<int:pk>/comentar/', views.comentar_publicacion, name='comentar_publicacion'),
    path('publicacion/<int:pk>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
    path('buscar/', views.buscar, name='buscar'),
    path('profile/', views.profile_view, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
]