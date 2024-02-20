from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from . import models
from .forms import DeporteForm, InstalacionForm, EquipoForm, JugadorForm, PartidoForm

class Inicio(generic.ListView):
    template_name = 'inicio.html'  
    context_object_name = 'contexto'  

    def get_queryset(self):
        return models.Partido.objects.none()  

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Página de inicio'
        contexto['menu_opciones'] = ['deportes', 'instalaciones', 'equipos', 'jugadores', 'partidos']
        contexto['imagen_deporte_url'] = 'URL_DE_LA_IMAGEN'
        contexto['ultimos_partidos'] = models.Partido.objects.filter(fecha_hora__lt=datetime.now()).order_by('-fecha_hora')[:5]
        contexto['proximos_partidos'] = models.Partido.objects.filter(fecha_hora__gte=datetime.now()).order_by('fecha_hora')[:5]
        return contexto

""" Deportes """

class DeportesListView(generic.ListView):
    template_name = 'deportes_list.html'
    context_object_name = 'deportes'

    def get_queryset(self):
        return models.Deporte.objects.all()

class DeportesCreateView(generic.CreateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = 'deportes_create.html'
    success_url = reverse_lazy('torre_crud:deportes-list') 

class DeportesDeleteView(generic.DeleteView):
    model = models.Deporte
    template_name = 'deportes_confirm_delete.html'
    success_url = reverse_lazy('torre_crud:deportes-list')

class DeportesUpdateView(generic.UpdateView):
    model = models.Deporte
    form_class = DeporteForm
    template_name = 'deportes_detail.html'
    success_url = reverse_lazy('torre_crud:deportes-list')

""" Instalaciones """

class InstalacionesListView(generic.ListView):
    template_name = 'instalaciones_list.html'
    context_object_name = 'instalaciones'

    def get_queryset(self):
        return models.Instalacion.objects.all()

class InstalacionesCreateView(generic.CreateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = 'instalacion_create.html'
    success_url = reverse_lazy('torre_crud:instalaciones-list')

class InstalacionesDeleteView(generic.DeleteView):
    model = models.Instalacion
    template_name = 'instalacion_confirm_delete.html'
    success_url = reverse_lazy('torre_crud:instalaciones-list')

class InstalacionesUpdateView(generic.UpdateView):
    model = models.Instalacion
    form_class = InstalacionForm
    template_name = 'instalacion_detail.html'
    success_url = reverse_lazy('torre_crud:instalaciones-list')

""" Equipo """

class EquiposListView(generic.ListView):
    template_name = 'equipos_list.html'
    context_object_name = 'equipos_list'

    def get_queryset(self):
        return models.Equipo.objects.all()

class EquiposCreateView(generic.CreateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = 'equipo_create.html'
    success_url = reverse_lazy('torre_crud:equipos-list')

class EquiposDeleteView(generic.DeleteView):
    model = models.Equipo
    template_name = 'equipo_confirm_delete.html'
    success_url = reverse_lazy('torre_crud:equipos-list')

class EquiposUpdateView(generic.UpdateView):
    model = models.Equipo
    form_class = EquipoForm
    template_name = 'equipo_update.html'
    success_url = reverse_lazy('torre_crud:equipos-list')

class EquipoDetailView(generic.DetailView):
    model = models.Equipo
    template_name = 'equipo_detail.html'

""" Jugador """

class JugadorListView(generic.ListView):
    model = models.Jugador
    template_name = 'jugador_list.html'
    context_object_name = 'jugadores'

class JugadorCreateView(generic.CreateView):
    model = models.Jugador
    form_class = JugadorForm
    template_name = 'jugador_create.html'

class JugadorUpdateView(generic.UpdateView):
    model = models.Jugador
    form_class = JugadorForm
    template_name = 'jugador_update.html'

class JugadorDetailView(generic.DetailView):
    model = models.Jugador
    template_name = 'jugador_detail.html'

class JugadorDeleteView(generic.DeleteView):
    model = models.Jugador
    success_url = reverse_lazy('torre_crud:jugadores-list')  
    template_name = 'jugador_confirm_delete.html'

""" Partidos """

class PartidoListView(generic.ListView):
    model = models.Partido
    template_name = 'partido_list.html'
    context_object_name = 'partidos'
    ordering = ['-fecha_hora']

class PartidoCreateView(generic.CreateView):
    model = models.Partido
    form_class = PartidoForm
    template_name = 'partido_create.html'

class PartidoUpdateView(generic.UpdateView):
    model = models.Partido
    form_class = PartidoForm
    template_name = 'partido_update.html'

class PartidoDetailView(generic.DetailView):
    model = models.Partido
    template_name = 'partido_detail.html'

class PartidoDeleteView(generic.DeleteView):
    model = models.Partido
    success_url = reverse_lazy('torre_crud:partidos-list')
    template_name = 'partido_confirm_delete.html'
