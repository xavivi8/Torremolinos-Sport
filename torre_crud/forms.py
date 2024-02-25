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
    
    def clean(self):
        cleaned_data = super().clean()
        id_local = cleaned_data.get('id_local')
        id_visitante = cleaned_data.get('id_visitante')

        # Verificar si el mismo equipo ha sido seleccionado como local y visitante
        if id_local == id_visitante:
            raise forms.ValidationError("El mismo equipo no puede ser seleccionado como local y visitante")

        return cleaned_data

