from django.urls import path
from . import views

urlpatterns = [
    # Inicio y consultas
    path('', views.ver_plantilla, name='inicio_socios'),
    path('lista-socios/', views.lista_socios, name='lista_socios'),
    
    # Registro / Creación de socios
    path('registrar-socio/', views.registrar_socio, name='registrar_socio'),
    
    # Edición / Actualización de socios
    path('editarSocio/<int:id>/', views.editarSocio, name='editar_socio'),
    
    # Eliminación de socios
    path('eliminarSocio/<int:id>/', views.eliminarSocio, name='eliminar_socio'),
    
    # --- EVALUACIONES MÉDICAS (RUTAS CORREGIDAS) ---
    # Ruta para registrar una nueva evaluación médica
    path('registrar-evaluacion/', views.registrar_evaluacion, name='registrar_evaluacion'),
    
    # Nueva ruta: Permite editar una evaluación existente usando su ID
    path('editar-evaluacion/<int:id>/', views.registrar_evaluacion, name='editar_evaluacion'),
    
    # Dashboard y Reportes
    path('reportes-ingresos/', views.reportes_ingresos, name='reportes_ingresos'),
]