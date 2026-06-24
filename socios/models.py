from django.db import models
from django.utils import timezone

PLAN_CHOICES = [
    ('MENSUAL', 'Mensual ($30)'),
    ('SEMESTRAL', 'Semestral ($150)'),
    ('ANUAL', 'Anual ($280)'),
]

TURNO_CHOICES = [
    ('MANANA', 'Mañana'),
    ('TARDE', 'Tarde'),
    ('NOCHE', 'Noche'),
]

APTITUD_CHOICES = [
    ('APTO', 'Apto'),
    ('RESTRINGIDO', 'Restringido'),
]

class Socio(models.Model):
    nombres_apellidos = models.CharField(max_length=200, verbose_name="Nombres y Apellidos")
    foto = models.ImageField(upload_to='socios_fotos/', blank=True, null=True, verbose_name="Foto Carnet")
    plan_contratado = models.CharField(max_length=20, choices=PLAN_CHOICES, verbose_name="Plan Contratado")
    turno_preferido = models.CharField(max_length=15, choices=TURNO_CHOICES, verbose_name="Turno Preferido")
    tiene_casillero = models.BooleanField(default=False, verbose_name="¿Cuenta con casillero alquilado?")
    fecha_inscripcion = models.DateField(default=timezone.now, verbose_name="Fecha de Inscripción")

    def __str__(self):
        return self.nombres_apellidos

    def obtener_costo_plan(self):
        costos = {'MENSUAL': 30, 'SEMESTRAL': 150, 'ANUAL': 280}
        return costos.get(self.plan_contratado, 0)


class EvaluacionMedica(models.Model):
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE, related_name='evaluacion_medica')
    certificado_pdf = models.FileField(upload_to='certificados_medicos/', verbose_name="Certificado Médico (PDF)")
    presion_arterial = models.CharField(max_length=20, verbose_name="Presión Arterial")
    nivel_aptitud = models.CharField(max_length=15, choices=APTITUD_CHOICES, verbose_name="Nivel de Aptitud")
    fecha_evaluacion = models.DateField(verbose_name="Fecha de la Evaluación")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones Médicas")

    def __str__(self):
        return f"Evaluación de {self.socio.nombres_apellidos}"