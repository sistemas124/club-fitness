import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Socio, EvaluacionMedica

# 1. Vista de la plantilla inicial
def ver_plantilla(request):
    return render(request, 'inicio.html')

# 2. Vista para listar los socios en la tabla (AQUÍ NO SE GENERAN MENSAJES)
def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'lista_socios.html', {'misSocios': socios})

# 3. Vista para registrar un nuevo socio 
def registrar_socio(request):
    if request.method == 'POST':
        nombres_input = request.POST.get("nombres_apellidos")
        foto_input = request.FILES.get("foto")
        plan_input = request.POST.get("plan_contratado")
        turno_input = request.POST.get("turno_preferido")
        casillero_input = request.POST.get("tiene_casillero") == "on"
        fecha_input = request.POST.get("fecha_inscripcion")
        
        Socio.objects.create(
            nombres=nombres_input,
            foto=foto_input,
            plan_contratado=plan_input,
            turno_preferido=turno_input,
            cuenta_con_casillero=casillero_input,
            fecha_inscripcion=fecha_input
        )
        
        messages.success(request, 'Socio guardado exitosamente')
        return redirect('lista_socios')
        
    return render(request, 'registrar_socio.html')

# 4. Vista para abrir el formulario de edición y procesar el guardado
def editarSocio(request, id):
    socio = get_object_or_404(Socio, id=id)
    
    if request.method == 'POST':
        socio.nombres = request.POST.get('nombres_apellidos')
        socio.plan_contratado = request.POST.get('plan_contratado')
        socio.turno_preferido = request.POST.get('turno_preferido')
        socio.cuenta_con_casillero = request.POST.get('tiene_casillero') == 'on'
        socio.fecha_inscripcion = request.POST.get('fecha_inscripcion')
        
        if 'foto' in request.FILES:
            if socio.foto and os.path.exists(socio.foto.path):
                os.remove(socio.foto.path)
            socio.foto = request.FILES['foto']
            
        socio.save()
        messages.success(request, f"¡Socio {socio.nombres} actualizado correctamente!")
        return redirect('lista_socios')
        
    return render(request, 'editar_socio.html', {'socio': socio})

# 5. Vista para eliminar el socio por ID
def eliminarSocio(request, id):
    socioAEliminar = get_object_or_404(Socio, id=id)
    socioAEliminar.delete()
    messages.success(request, 'Socio eliminado correctamente')
    return redirect('lista_socios')

# 6. Vista unificada para registrar y editar la evaluación médica
def registrar_evaluacion(request, id=None):
    # Buscamos la evaluación si viene un ID (Modo Edición), sino queda en None (Modo Registro)
    evaluacion = get_object_or_404(EvaluacionMedica, id=id) if id else None

    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        certificado = request.FILES.get('certificado_pdf')
        presion = request.POST.get('presion_arterial')
        aptitud = str(request.POST.get('nivel_aptitud')).upper()
        fecha = request.POST.get('fecha_evaluacion')
        obs = request.POST.get('observaciones')
        
        socio_instancia = get_object_or_404(Socio, id=socio_id)
        
        if evaluacion:
            # Lógica de Actualización (Edición)
            evaluacion.socio = socio_instancia
            evaluacion.presion_arterial = presion
            evaluacion.nivel_aptitud = aptitud
            evaluacion.fecha_evaluacion = fecha
            evaluacion.observaciones_medicas = obs
            
            if certificado:
                # Borramos el PDF antiguo del disco duro para que no ocupe espacio innecesario
                if evaluacion.certificado_pdf and os.path.exists(evaluacion.certificado_pdf.path):
                    os.remove(evaluacion.certificado_pdf.path)
                evaluacion.certificado_pdf = certificado
                
            evaluacion.save()
            messages.success(request, '¡Evaluación médica actualizada correctamente!')
        else:
            # Lógica de Inserción (Registro nuevo)
            EvaluacionMedica.objects.create(
                socio=socio_instancia,
                certificado_pdf=certificado,
                presion_arterial=presion,
                nivel_aptitud=aptitud,
                fecha_evaluacion=fecha,
                observaciones_medicas=obs
            )
            messages.success(request, '¡Evaluación médica guardada y estado de torniquete actualizado!')
            
        return redirect('reportes_ingresos')
        
    socios = Socio.objects.all()
    contexto = {
        'lista_socios': socios,
        'evaluacion': evaluacion
    }
    return render(request, 'registrar_evaluacion.html', contexto)

# 7. Vista para el Dashboard de Reportes e Ingresos
def reportes_ingresos(request):
    todos_socios = Socio.objects.all()
    total_socios = todos_socios.count()
    
    proyeccion = 0
    for s in todos_socios:
        if s.plan_contratado == "MENSUAL":
            proyeccion += 30
        elif s.plan_contratado == "SEMESTRAL":
            proyeccion += 150
        elif s.plan_contratado == "ANUAL":
            proyeccion += 280
            
    no_aptos = EvaluacionMedica.objects.filter(nivel_aptitud__icontains="RESTRINGIDO")

    contexto = {
        'total_socios': total_socios,
        'proyeccion_total': proyeccion,
        'socios_no_aptos': no_aptos
    }
    
    return render(request, 'reportes.html', contexto)