"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SaludApp.views import index, pacientes, medicos, otros, agregar_medico, agregar_paciente, agregar_otro, buscar_medico, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name = "Inicio"),
    path('pacientes', pacientes, name="Pacientes"),
    path('medicos', medicos, name = "Medicos"),
    path('medicos/agregar', agregar_medico, name = "agregar-medico"),
    path('pacientes/agregar', agregar_paciente, name = "agregar-paciente"),
    path('otros', otros, name = "Otros"),
    path('otros/agregar', agregar_otro, name = "agregar-otro"),
    path('buscar_medico', buscar_medico, name = "buscar-medico"),
    path('buscar', buscar, name = "buscar"),
]
