from django.db import models
from django.core.validators import MinValueValidator


class Deportes(models.Model):
    id_deporte = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        verbose_name = "Deporte"
        verbose_name_plural = "Deportes"
        db_table = 'deportes'
    
    def __str__(self):
        return self.nombre


class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)
    id_deporte = models.ForeignKey(Deportes, models.DO_NOTHING, db_column='id_deporte', default = 0)
    equipacion_principal = models.CharField(max_length=100)
    equipacion_suplente = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        managed = False
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = 'equipos'
    
    def __str__(self):
        return self.nombre


class Instalaciones(models.Model):
    id_instalacion = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=20)
    direccion = models.CharField(max_length=100)
    iluminacion = models.BooleanField(default=False)
    cubierta = models.BooleanField(default=False)

    class Meta:
        managed = False
        verbose_name = "Instalación"
        verbose_name_plural = "Instalaciones"
        db_table = 'instalaciones'

    def __str__(self):
        return self.nombre



class Jugadores(models.Model):
    id_jugador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido1 = models.CharField(max_length=20)
    apellido2 = models.CharField(max_length=20, blank=True, null=True)
    id_equipo = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_equipo', default = 0)
    dorsal = models.IntegerField()
    fecha_nacimiento = models.DateField()
    altura = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0)])
    peso = models.IntegerField(validators=[MinValueValidator(0)])
    telefono = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'jugadores'
        unique_together = (('id_equipo', 'dorsal'),)


class Partidos(models.Model):
    id_partido = models.AutoField(primary_key=True)
    id_deporte = models.ForeignKey(Deportes, models.DO_NOTHING, db_column='id_deporte')
    fecha_hora = models.DateTimeField()
    id_instalacion = models.ForeignKey(Instalaciones, models.DO_NOTHING, db_column='id_instalacion', blank=True, null=True)
    id_local = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_local')
    id_visitante = models.ForeignKey(Equipos, models.DO_NOTHING, db_column='id_visitante', related_name='partidos_id_visitante_set')
    puntos_local = models.IntegerField(blank=True, null=True, default=0, validators=[MinValueValidator(0)])
    puntos_visitante = models.IntegerField(blank=True, null=True, default=0, validators=[MinValueValidator(0)])
    observaciones = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partidos'