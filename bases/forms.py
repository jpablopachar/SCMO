from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from bases.models import Consultorio


class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'input-lg'})


class ConsultorioForm(forms.ModelForm):
    class Meta:
        model = Consultorio
        fields = ['nombre']
        widgets = {'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese Nuevo Consultorio'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class EditarConsultorioForm(forms.ModelForm):
    class Meta:
        model = Consultorio
        fields = ['nombre']
        widget = {'nombre': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control input-lg'})
