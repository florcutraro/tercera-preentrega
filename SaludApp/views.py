from django.shortcuts import render
from django.http import HttpResponse
from SaludApp.forms import MedicosForm, PacientesForm, OtrosForm
from SaludApp.models import Medicos, Pacientes, Otros_Profesionales

def index(request):
    return render(request, "SaludApp/inicio.html")

def pacientes(request):
     context = {
         "form": PacientesForm(),
         "pacientes": Pacientes.objects.all(),
         }

    
     return render(request, "SaludApp/pacientes.html", context)

def agregar_paciente(request):
     pacientes_form = PacientesForm(request.POST)
     pacientes_form.save()
     context = {
          "form": PacientesForm(),
          "pacientes": Pacientes.objects.all(),
     }
     return render(request, 'SaludApp/pacientes.html', context)

def medicos(request):
    context = {
         "form": MedicosForm(),
         "medicos": Medicos.objects.all(),
         }

    
    return render(request, "SaludApp/medicos.html", context)

def agregar_medico(request):
     medicos_form = MedicosForm(request.POST)
     medicos_form.save()
     context = {
          "form": MedicosForm(),
          "medicos": Medicos.objects.all(),
     }
     return render(request, 'SaludApp/medicos.html', context)

def otros(request):
     context = {
         "form": OtrosForm(),
         "otros": Otros_Profesionales.objects.all(),
         }

    
     return render(request, 'SaludApp/otros.html', context)

def agregar_otro(request):
     otros_form = OtrosForm(request.POST)
     otros_form.save()
     context = {
          "form": OtrosForm(),
          "otros": Otros_Profesionales.objects.all(),
     }
     return render(request, 'SaludApp/otros.html', context)

def buscar_medico(request):
     return render(request, 'SaludApp/buscar.html')

def buscar(request):

     if request.GET['Especialidad']:

          Especialidad = request.GET['Especialidad']
          medicos = Medicos.objects.filter(Especialidad__icontains=Especialidad)

          return render(request, 'SaludApp/buscar.html', {"medicos":medicos, "Especialidad": Especialidad})
     
     else:
          respuesta = "No enviaste datos"
     
     return HttpResponse(respuesta)