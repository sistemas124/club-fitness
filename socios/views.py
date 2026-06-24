from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio, EvaluacionMedica
from django.db.models import Count

def ver_plantilla(request):
    return render(request, 'inicio.html')

# 1. Registrar Socios (Backend captura inputs manuales del HTML)
def registrar_socio(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres_apellidos')
        foto = request.FILES.get('foto')
        plan = request.POST.get('plan_contratado')
        turno = request.POST.get('turno_preferido')
        casillero = request.POST.get('tiene_casillero') == 'on' # Checkbox retorna 'on' si se marca
        fecha = request.POST.get('fecha_inscripcion')
        
        # Guardamos directamente en la base de datos estilo clase
        nuevo_socio = Socio(
            nombres_apellidos=nombres,
            foto=foto,
            plan_contratado=plan,
            turno_preferido=turno,
            tiene_casillero=casillero,
            fecha_inscripcion=fecha
        )
        nuevo_socio.save()
        return redirect('lista_socios')
        
    return render(request, 'registrar_socio.html')

# 2. Listar Socios (Ficha para el Instructor)
def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'lista_socios.html', {'socios': socios})

# 3. Registrar Evaluaciones Médicas (Recibe PDFs)
def registrar_evaluacion(request):
    socios = Socio.objects.all()
    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        socio_obj = get_object_or_404(Socio, id=socio_id)
        pdf = request.FILES.get('certificado_pdf')
        presion = request.POST.get('presion_arterial')
        aptitud = request.POST.get('nivel_aptitud')
        fecha = request.POST.get('fecha_evaluacion')
        observaciones = request.POST.get('observaciones')
        
        nueva_evaluacion = EvaluacionMedica(
            socio=socio_obj,
            certificado_pdf=pdf,
            presion_arterial=presion,
            nivel_aptitud=aptitud,
            fecha_evaluacion=fecha,
            observaciones=observaciones
        )
        nueva_evaluacion.save()
        return redirect('reportes_ingresos')
        
    return render(request, 'registrar_evaluacion.html', {'socios': socios})

# 4. Reporte y Cálculos (Proyección y Torniquete)
def reportes_ingresos(request):
    # Valores de planes asignados para el cálculo
    # Mensual = $30, Semestral = $150, Anual = $280
    socios = Socio.objects.all()
    proyeccion_total = 0
    
    for s in socios:
        if s.plan_contratado == 'Mensual':
            proyeccion_total += 30
        elif s.plan_contratado == 'Semestral':
            proyeccion_total += 150
        elif s.plan_contratado == 'Anual':
            proyeccion_total += 280
            
    # Filtro para el Torniquete: Reporte de Socios Restringidos (No Aptos)
    socios_no_aptos = EvaluacionMedica.objects.filter(nivel_aptitud='Restringido')
    
    context = {
        'proyeccion_total': proyeccion_total,
        'socios_no_aptos': socios_no_aptos,
        'total_socios': socios.count()
    }
    return render(request, 'reportes.html', context)