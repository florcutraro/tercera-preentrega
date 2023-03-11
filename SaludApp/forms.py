from django import forms
from SaludApp.models import Medicos, Pacientes, Otros_Profesionales

class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = '__all__'

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = '__all__'

class OtrosForm(forms.ModelForm):
    class Meta:
        model = Otros_Profesionales
        fields = '__all__'