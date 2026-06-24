from django.db import models

# Create your models here.

class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    nombres_apellidos = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='socios/fotos/', null=True, blank=True)
    
    # Opciones para listas desplegables y radios
    PLANES = [
        ('Mensual', 'Mensual'),
        ('Semestral', 'Semestral'),
        ('Anual', 'Anual'),
    ]
    plan_contratado = models.CharField(max_length=20, choices=PLANES)
    
    TURNOS = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]
    turno_preferido = models.CharField(max_length=20, choices=TURNOS)
    
    tiene_casillero = models.BooleanField(default=False)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.nombres_apellidos} - Plan: {self.plan_contratado} - Turno: {self.turno_preferido}"


class EvaluacionMedica(models.Model):
    id = models.AutoField(primary_key=True)
    # Relación con Socio (Como la relación Equipo-Estadio de tu clase)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    certificado_pdf = models.FileField(upload_to='socios/certificados/')
    presion_arterial = models.CharField(max_length=20)
    
    APTITUD = [
        ('Apto', 'Apto'),
        ('Restringido', 'Restringido'),
    ]
    nivel_aptitud = models.CharField(max_length=20, choices=APTITUD)
    fecha_evaluacion = models.DateField()
    observaciones = models.TextField()

    def __str__(self):
        return f"Evaluación de {self.socio.nombres_apellidos} - Estado: {self.nivel_aptitud}"