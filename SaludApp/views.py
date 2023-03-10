from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "SaludApp/inicio.html")

def pacientes(request):
      return render(request, "SaludApp/pacientes.html")

def medicos(request):
     return render(request, 'SaludApp/medicos.html')

def otros(request):
     return render(request, 'SaludApp/otros.html')