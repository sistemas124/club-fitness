from django.urls import path
from . import views

urlpatterns = [
    # Inicio y consultas
    path('', views.ver_plantilla, name='inicio_socios'),
    path('lista-socios/', views.lista_socios, name='lista_socios'),
    
    # Registro / Creación de socios
    path('registrar-socio/', views.registrar_socio, name='registrar_socio'),
    
    # Edición / Actualización de socios (Basado en la lógica de tus estadios)
    path('editarSocio/<int:id>/', views.editarSocio, name='editar_socio'),
    path('procesarActualizacionSocio/', views.procesarActualizacionSocio, name='procesar_actualizacion_socio'),
    
    # Eliminación de socios
    path('eliminarSocio/<int:id>/', views.eliminarSocio, name='eliminar_socio'),
    
    # Otras rutas que ya tenías
    path('registrar-evaluacion/', views.registrar_evaluacion, name='registrar_evaluacion'),
    path('reportes-ingresos/', views.reportes_ingresos, name='reportes_ingresos'),
]