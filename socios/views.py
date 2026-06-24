from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio
from django.contrib import messages

# 1. Vista de la plantilla inicial
def ver_plantilla(request):
    return render(request, 'inicio.html')

# 2. Vista para listar los socios en la tabla
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
        
        # MENSAJE DE ÉXITO: Solo al crear
        messages.success(request, 'Socio guardado exitosamente')
        return redirect('lista_socios')
        
    return render(request, 'registrar_socio.html')

# 4. Vista para abrir el formulario de edición (AQUÍ NO SE GENERA NINGÚN MENSAJE)
def editarSocio(request, id):
    socio_a_editar = get_object_or_404(Socio, id=id)
    return render(request, 'registrar_socio.html', {'socio': socio_a_editar})

# 5. Vista para procesar la actualización del socio editado
def procesarActualizacionSocio(request):
    if request.method == 'POST':
        id_socio = request.POST.get("id")
        socioActualizar = get_object_or_404(Socio, id=id_socio)
        
        socioActualizar.nombres = request.POST.get("nombres_apellidos")
        socioActualizar.plan_contratado = request.POST.get("plan_contratado")
        socioActualizar.turno_preferido = request.POST.get("turno_preferido")
        socioActualizar.cuenta_con_casillero = request.POST.get("tiene_casillero") == "on"
        socioActualizar.fecha_inscripcion = request.POST.get("fecha_inscripcion")
        
        foto_nueva = request.FILES.get("foto")
        if foto_nueva:
            socioActualizar.foto = foto_nueva
            
        socioActualizar.save()
        
        # MENSAJE DE ÉXITO: Solo al actualizar físicamente en BDD
        messages.success(request, 'Socio actualizado correctamente')
        
    return redirect('lista_socios')

# 6. Vista para eliminar el socio por ID
def eliminarSocio(request, id):
    socioAEliminar = get_object_or_404(Socio, id=id)
    socioAEliminar.delete()
    
    # MENSAJE DE ÉXITO: Solo al eliminar
    messages.success(request, 'Socio eliminado correctamente')
    return redirect('lista_socios')

def registrar_evaluacion(request):
    return render(request, 'registrar_evaluacion.html')

def reportes_ingresos(request):
    return render(request, 'reportes.html')