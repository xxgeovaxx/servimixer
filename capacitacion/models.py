from django.db import models

# Create your models here.


class BaseName(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '{0}'.format(self.nombre)


class Departamento(BaseName):
    pass


class NivelDeEstudio(BaseName):
    pass


class Cargo(BaseName):
    pass


class Curso(BaseName):
    pass


class Labores(BaseName):
    pass


class DatosPersonas(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    departamento = models.ForeignKey(Departamento)
    cargo = models.ForeignKey(Cargo)
    nivel_cademico = models.ForeignKey(NivelDeEstudio)
    capacitacion = models.BooleanField(
        verbose_name='desea usted una capacitacion laboral?'
    )
    curso_ = 'De acuerdo a la respuesta, en cual de las siguientes areas desea capacitarse'
    curso = models.ForeignKey(
        Curso,
        verbose_name=curso_
    )
    msj_area = 'Selecione en que area necesita ' \
               'usted capacitarse para desarrollar sus labores diarias'
    area = models.ForeignKey(Labores, verbose_name=msj_area, blank=True, null=True)

    tema = models.TextField(
        verbose_name='que otro tema usted considera como importante para ser incluido'
                     'dentro de una capacitacion?', blank=True, null=True
    )

    motivado = models.BooleanField()

    motivacion = models.TextField(
        verbose_name='que lo motiva a usted a prepararse mas academicamente?'
        , blank=True, null=True
    )

    def nombre_completo(self):
        return '{0} {1}'.format(self.nombres, self.apellidos)


