from django.urls import path
from django.contrib.auth import views as auth_views
from bases.views import Home, Seleccionar, Perfil, editarPerfil, nuevoConsultorio, EditarConsultorio, eliminarConsultorio

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('seleccionar/', Seleccionar.as_view(), name='seleccionar'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/seleccionar.html'), name='logout'),
    path('perfil/', Perfil.as_view(), name='perfil'),
    path('editarPerfil/', editarPerfil, name='editarPerfil'),
    path('consultorio/', nuevoConsultorio, name='consultorios'),
    path('consultorio/editar/<int:pk>', EditarConsultorio.as_view(), name='editarConsultorio'),
    path('consultorio/eliminar/<int:id>', eliminarConsultorio, name='eliminarConsultorio'),
]
