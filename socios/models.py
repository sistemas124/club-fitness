from django.db import models

PLANES_CHOICES = [
    ('MENSUAL', 'Mensual ($30.00)'),
    ('SEMESTRAL', 'Semestral ($150.00)'),
    ('ANUAL', 'Anual ($280.00)'),
]

TURNOS_CHOICES = [
    ('MANANA', 'Mañana'),
    ('TARDE', 'Tarde'),
    ('NOCHE', 'Noche'),
]

APTITUD_CHOICES = [
    ('APTO', 'Apto para entrenar'),
    ('RESTRINGIDO', 'Restringido / No Apto'),
]

class Socio(models.Model):
    nombres = models.CharField(max_length=100, verbose_name="Nombres y Apellidos")
    foto = models.ImageField(upload_to='fotos_socios/', null=True, blank=True, verbose_name="Foto Carnet")
    plan_contratado = models.CharField(max_length=15, choices=PLANES_CHOICES, default='MENSUAL', verbose_name="Plan Contratado")
    turno_preferido = models.CharField(max_length=10, choices=TURNOS_CHOICES, default='MANANA', verbose_name="Turno Preferido")
    cuenta_con_casillero = models.BooleanField(default=False, verbose_name="¿Cuenta con casillero alquilado?")
    fecha_inscripcion = models.DateField(verbose_name="Fecha de Inscripción")

    def __str__(self):
        return self.nombres

class EvaluacionMedica(models.Model):
    socio = models.OneToOneField(Socio, on_delete=models.CASCADE, related_name='evaluacion', verbose_name="Socio")
    certificado_pdf = models.FileField(upload_to='certificados_medicos/', verbose_name="Certificado Médico (PDF)")
    presion_arterial = models.CharField(max_length=20, verbose_name="Presión Arterial")
    nivel_aptitud = models.CharField(max_length=15, choices=APTITUD_CHOICES, default='APTO', verbose_name="Nivel de Aptitud")
    fecha_evaluacion = models.DateField(verbose_name="Fecha de la Evaluación")
    observaciones_medicas = models.TextField(blank=True, null=True, verbose_name="Observaciones Médicas")

    def __str__(self):
        return f"Evaluación de {self.socio.nombres} - {self.nivel_aptitud}"