from django.contrib import admin
from .models import Socio, EvaluacionMedica

# Registramos los modelos para poder verlos y probarlos en el navegador
admin.site.register(Socio)
admin.site.register(EvaluacionMedica)