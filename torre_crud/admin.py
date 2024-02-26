from django.contrib import admin
from .models import Deportes, Equipos, Instalaciones, Jugadores, Partidos

# Register your models here.

class DeportesAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre']

admin.site.register(Deportes, DeportesAdmin)

class InstalacionesAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre']

admin.site.register(Instalaciones, InstalacionesAdmin)

class EquiposAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'contacto', 'id_deporte__nombre']
    list_display = ['nombre', 'id_deporte', 'contacto']

admin.site.register(Equipos, EquiposAdmin)

class JugadoresAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido1', 'apellido2', 'id_equipo__nombre']
    list_display = ['nombre', 'apellido1', 'apellido2', 'id_equipo']

admin.site.register(Jugadores, JugadoresAdmin)

class PartidosAdmin(admin.ModelAdmin):
    search_fields = ['id_deporte__nombre', 'id_instalacion__nombre', 'id_local__nombre', 'id_visitante__nombre']
    list_display = ['id_deporte', 'id_instalacion', 'id_local', 'id_visitante']

admin.site.register(Partidos, PartidosAdmin)