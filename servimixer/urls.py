"""servimixer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from capacitacion.views import log_in, dashboard, salir, EncuestaCreateView, EncuestaExitosa
from capacitacion.views import Encuestas, EncuestaDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', log_in, name='entrar'),
    url(r'^inicio/', dashboard, name='inicio'),
    url(r'^crear/', EncuestaCreateView.as_view(), name='crear'),
    url(r'^salir/', salir, name='salir'),
    url(r'^encuestas/', Encuestas.as_view(), name='encuestas'),
    url(r'^encuesta/(?P<pk>\d+)/', EncuestaDetailView.as_view(), name='encuesta'),
    url(r'^exitoso/', EncuestaExitosa.as_view(), name='exito')
]
