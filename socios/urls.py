from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_plantilla, name='inicio_socios'),
    path('registrar-socio/', views.registrar_socio, name='registrar_socio'),
    path('lista-socios/', views.lista_socios, name='lista_socios'),
    path('registrar-evaluacion/', views.registrar_evaluacion, name='registrar_evaluacion'),
    path('reportes-ingresos/', views.reportes_ingresos, name='reportes_ingresos'),
]