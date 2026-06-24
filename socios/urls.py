from django.urls import path
from . import views

urlpatterns = [
    # Ruta raíz (La que abre al entrar a http://127.0.0.1:8000/)
    path('', views.inicio, name='inicio_socios'),
    
    # Rutas para el menú de la plantilla
    path('registrar/', views.registrar_socio, name='registrar_socio'),
    path('socios/', views.lista_socios, name='lista_socios'),
    path('evaluacion/', views.nueva_evaluacion, name='nueva_evaluacion'),
    path('reportes/', views.reporte_ingresos, name='reporte_ingresos'),
]