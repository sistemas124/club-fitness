from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('socios.urls')), # Conecta socios directamente a la raíz
]