from django.shortcuts import render, redirect
from .forms import SocioForm, EvaluacionMedicaForm
from .models import Socio, EvaluacionMedica

# Vista para la página principal (Tu carrusel de FITNESS CONTROL)
def inicio(request):
    return render(request, 'inicio.html')

# Vista para registrar socios (Formulario)
def registrar_socio(request):
    return render(request, 'registrar_socio.html')

# Vista para listar los socios registrados
def lista_socios(request):
    return render(request, 'lista_socios.html')

# Vista para registrar certificados médicos
def nueva_evaluacion(request):
    return render(request, 'nueva_evaluacion.html')

# Vista para cálculos de dinero y reportes de acceso
def reporte_ingresos(request):
    return render(request, 'reporte_ingresos.html')