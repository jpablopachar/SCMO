from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from bases.forms import EditarPerfilForm
from bases.models import Consultorio
from bases.forms import ConsultorioForm, EditarConsultorioForm


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'


class Seleccionar(generic.TemplateView):
    template_name = 'bases/seleccionar.html'


class Perfil(LoginRequiredMixin, generic.TemplateView):
    login_url = 'bases:seleccionar'
    template_name = 'bases/perfil.html'


@login_required(login_url='bases:seleccionar')
def editarPerfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect(reverse('bases:perfil'))
    else:
        form = EditarPerfilForm(instance=request.user)
        args = {'form': form}

        return render(request, 'bases/editarPerfil.html', args)


@login_required(login_url='bases:seleccionar')
def nuevoConsultorio(request):
    form = ConsultorioForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('bases:consultorios')

    return render(request, 'bases/consultorios.html', {'form': form, 'consultorios': Consultorio.objects.all()})


'''@login_required(login_url='bases:seleccionar')
def editarConsultorio(request, id):
    consultorio = Consultorio.objects.get(id=id)
    form = ConsultorioForm(request.POST or None, instance=consultorio)

    if form.is_valid():
        form.save()

        return redirect('bases:consultorios')

    return render(request, 'bases/consultorios.html', {'form': form, 'consultorios': Consultorio.objects.all()})'''


class EditarConsultorio(LoginRequiredMixin, generic.UpdateView):
    model = Consultorio
    template_name = "bases/editarConsultorio.html"
    context_object_name = "consultorio"
    form_class = EditarConsultorioForm
    success_url = reverse_lazy("bases:consultorios")

    def form_valid(self, form):
        return super().form_valid(form)


@login_required(login_url='bases:seleccionar')
def eliminarConsultorio(request, id):
    if request.method == 'GET':
        consultorio = Consultorio.objects.get(id=id)
        consultorio.delete()

        return redirect('bases:consultorios')

    return render(request, 'bases/consultorios.html')
