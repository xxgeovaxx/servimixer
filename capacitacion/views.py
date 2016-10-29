from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView

from capacitacion.forms import DatosPersonasForm
from capacitacion.models import DatosPersonas


def log_in(request):
    context = {'error': False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('inicio')
            else:
                context = {'msj': 'El usuario ha sido desactivado', 'error': True}
        else:
            context = {'msj': 'usuario o contraseña incorrecta', 'error': True}
    return render(request, 'login.html', context)


@login_required
def dashboard(request):
    usuarios = User.objects.all().count()
    data = {
        'usuarios': usuarios,
        'encuestas': DatosPersonas.objects.all().count()
    }
    return render(request, 'inicio.html', data)


@login_required
def salir(request):
    logout(request)
    return redirect('entrar')


class EncuestaCreateView(LoginRequiredMixin, CreateView):
    form_class = DatosPersonasForm
    template_name = 'form.html'
    success_url = reverse_lazy('exito')


class EncuestaExitosa(LoginRequiredMixin, TemplateView):
    template_name = 'exitosa.html'


class Encuestas(LoginRequiredMixin, ListView):
    model = DatosPersonas
    template_name = 'encuestas.html'
    queryset = DatosPersonas.objects.all()


class EncuestaDetailView(LoginRequiredMixin, DetailView):
    model = DatosPersonas
    template_name = 'detalle.html'