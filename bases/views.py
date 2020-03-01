from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

class Seleccionar(generic.TemplateView):
    template_name = 'bases/seleccionar.html'


class Perfil(LoginRequiredMixin, generic.TemplateView):
    login_url = 'bases:seleccionar'
    template_name = 'bases/perfil.html'
