from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# Importamos las vistas de autenticación nativas de Django
from django.contrib.auth import views as auth_views 

urlpatterns = [
    # 1. ESTA RUTA TIENE QUE IR PRIMERO para ganarle a las demás de accounts
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # 2. Las demás rutas automáticas de Django (como el logout)
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # 3. Tus rutas de la administración y la app socios
    path('admin/', admin.site.urls),
    path('', include('socios.urls')), 
]

# Configuración para servir las fotos de los socios
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)