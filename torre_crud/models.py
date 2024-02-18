from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Deporte(models.Model):
    nombre = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "Deporte"
        verbose_name_plural = "Deportes"
        db_table = "deportes"

    def __str__(self):
        return self.nombre

class Instalacion(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=100)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Instalación"
        verbose_name_plural = "Instalaciones"
        db_table = "instalaciones"

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    equipacion_principal = models.CharField(max_length=100)
    equipacion_suplente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "equipos"

    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    dorsal = models.IntegerField()
    fecha_nacimiento = models.DateField()
    altura = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0)])
    peso = models.IntegerField(validators=[MinValueValidator(0)])
    telefono = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "jugadores"
        unique_together = ('equipo', 'dorsal')

    def __str__(self):
        return f"{self.nombre} {self.apellido1} ({self.equipo.nombre})"

class Partido(models.Model):
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    instalacion = models.ForeignKey(Instalacion, on_delete=models.SET_NULL, blank=True, null=True)
    local = models.ForeignKey(Equipo, related_name='local', on_delete=models.CASCADE)
    visitante = models.ForeignKey(Equipo, related_name='visitante', on_delete=models.CASCADE)
    puntos_local = models.PositiveIntegerField(default=0)
    puntos_visitante = models.PositiveIntegerField(default=0)
    observaciones = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"
        db_table = "partidos"

    def __str__(self):
        return f"{self.local.nombre} vs {self.visitante.nombre} - {self.fecha_hora}"

