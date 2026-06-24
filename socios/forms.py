from django import forms
from .models import Socio, EvaluacionMedica

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombres', 'foto', 'plan_contratado', 'turno_preferido', 'cuenta_con_casillero', 'fecha_inscripcion']

class EvaluacionMedicaForm(forms.ModelForm):
    class Meta:
        model = EvaluacionMedica
        fields = ['socio', 'certificado_pdf', 'presion_arterial', 'nivel_aptitud', 'fecha_evaluacion', 'observaciones_medicas']