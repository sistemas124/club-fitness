from django.urls import path
from . import views

urlpatterns = [
    # Al dejarlo vacío, esta app responderá en la raíz
    path('', views.ver_plantilla, name='inicio_socios'),
]