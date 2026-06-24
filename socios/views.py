from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Socio, EvaluacionMedica
from django.db.models import Q

def ver_plantilla(request):
    # Tu vista original para la plantilla principal PoniGym (imagen.jpg)
    return render(request, 'inicio.html')

# Vista para el Perfil: Administrador del Club
def dashboard_administrador(request):
    # 1. Traer todos los socios
    socios = Socio.objects.all()
    
    # 2. Cálculos y Reporte: Proyección de ingresos multiplicando socios activos por costo del plan
    proyeccion_total = sum(socio.obtener_costo_plan() for socio in socios)
    
    # 3. Reporte de "Socios no Aptos" o con certificado vencido/inexistente
    socios_no_aptos = Socio.objects.filter(
        Q(evaluacion_medica__nivel_aptitud='RESTRINGIDO') | 
        Q(evaluacion_medica__isnull=True)
    )
    
    context = {
        'socios': socios,
        'proyeccion_total': proyeccion_total,
        'socios_no_aptos': socios_no_aptos,
    }
    return render(request, 'dashboard_admin.html', context)

# Vista para el Perfil: Instructor / Entrenador
def ficha_socio_instructor(request, socio_id):
    # Consulta la ficha del socio y valida su certificado de salud
    try:
        socio = Socio.objects.get(id=socio_id)
        evaluacion = getattr(socio, 'evaluacion_medica', None)
    except Socio.DoesNotExist:
        socio = None
        evaluacion = None

    context = {
        'socio': socio,
        'evaluacion': evaluacion,
    }
    return render(request, 'ficha_socio.html', context)