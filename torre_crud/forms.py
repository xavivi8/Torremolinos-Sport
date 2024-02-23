from django import forms
from . import models

class DeporteForm(forms.ModelForm):
    class Meta:
        model = models.Deportes
        exclude = ['id_deporte']

class InstalacionForm(forms.ModelForm):
    class Meta:
        model = models.Instalaciones
        exclude = ['id_instalacion']

class EquipoForm(forms.ModelForm):
    class Meta:
        model = models.Equipos
        exclude = ['id_equipo']

class JugadorForm(forms.ModelForm):
    class Meta:
        model = models.Jugadores
        exclude = ['id_jugador']

class PartidoForm(forms.ModelForm):
    class Meta:
        model = models.Partidos
        exclude = ['id_partido']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }

