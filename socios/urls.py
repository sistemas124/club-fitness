from django.urls import path
from . import views

# Esta es la lista 'urlpatterns' que Django no encontraba
urlpatterns = [
    path('inicio/', views.ver_plantilla, name='inicio_socios'),
]