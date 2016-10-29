from django.contrib import admin

from capacitacion.forms import DatosPersonasForm
from .models import Departamento, NivelDeEstudio, Curso, Cargo, DatosPersonas, Labores
# Register your models here.


base_lista = ['id', 'nombre']


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = base_lista


@admin.register(NivelDeEstudio)
class NivelDeEstudioAdmin(admin.ModelAdmin):
    list_display = base_lista


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = base_lista


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = base_lista


@admin.register(DatosPersonas)
class DatosPersonasAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'departamento', 'identificacion']
    form = DatosPersonasForm


@admin.register(Labores)
class LaboresAdmin(admin.ModelAdmin):
    list_display = base_lista
