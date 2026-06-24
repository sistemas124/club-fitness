from django.urls import path
from . import views

urlpatterns = [
    # 1. Tu ruta original para ver la plantilla de PoniGym (Home)
    path('', views.ver_plantilla, name='inicio_socios'),
    
    # 2. Ruta para el Dashboard del Administrador (Ver socios, casilleros y proyección de ingresos)
    path('dashboard/administrador/', views.dashboard_administrador, name='dashboard_admin'),
    
    # 3. Ruta para el Instructor (Para buscar un socio y validar su certificado de salud/PDF)
    path('socio/<int:socio_id>/ficha/', views.ficha_socio_instructor, name='ficha_socio'),
]