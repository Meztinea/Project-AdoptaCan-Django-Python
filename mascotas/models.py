from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.


# Tabla Mascota
class Mascota(models.Model):

    class Sexo(models.IntegerChoices):
        HEMBRA = 0, _('Hembra')
        MACHO = 1, _('Macho')

    class Edad(models.IntegerChoices):
        CACHORRO = 0, _('Cachorro')
        JOVEN = 1, _('Joven')
        ADULTO = 2, _('Adulto')

    class Tamano(models.IntegerChoices):
        PEQUENO = 0, _('Pequeño')
        MEDIANO = 1, _('Mediano')
        GRANDE = 2, _('Grande')

    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50, default='Mestizo/criollo')
    sexo = models.IntegerField(choices=Sexo.choices)  # Hembra - Macho
    edad = models.IntegerField(choices=Edad.choices)  # Cachorro - Joven - Adulto
    tamaño = models.IntegerField(choices=Tamano.choices)  # Pequeño - Mediano - Grande
    adoptado = models.BooleanField(default=False)
    imagen = models.ImageField(upload_to='mascotas/imagenes')
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Mascotas'


# Tabla Adoptante 
class Adoptante(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Adoptantes'
    
# Tabla Solicitudes de Adopción
class Solicitud(models.Model):
    fecha_solicitud = models.DateTimeField(default=timezone.now)
    aprobada = models.BooleanField(default=False)
    fecha_aprobacion = models.DateTimeField(blank=True, null=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    adoptante_id = models.ForeignKey(Adoptante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.adoptante_id.nombre + ' - ' + self.mascota_id.nombre
    
    class Meta:
        verbose_name_plural = 'Solicitudes'