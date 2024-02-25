from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views import generic
from . import models
from .forms import DeporteForm, InstalacionForm, EquipoForm, JugadorForm, PartidoForm

class Inicio(generic.ListView):
    template_name = 'inicio.html'  
    context_object_name = 'contexto'  

    def get_queryset(self):
        return models.Partidos.objects.none()  

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Página de inicio'
        contexto['menu_opciones'] = ['deportes', 'instalaciones', 'equipos', 'jugadores', 'partidos']
        contexto['imagen_deporte_url'] = 'URL_DE_LA_IMAGEN'
        contexto['ultimos_partidos'] = models.Partidos.objects.filter(fecha_hora__lt=datetime.now()).order_by('-fecha_hora')[:5]
        contexto['proximos_partidos'] = models.Partidos.objects.filter(fecha_hora__gte=datetime.now()).order_by('fecha_hora')[:5]
        return contexto

""" Deportes """

class DeportesListView(generic.ListView):
    template_name = 'deportes_list.html'
    context_object_name = 'deportes'

    def get_queryset(self):
        return models.Deportes.objects.all()

class DeportesCreateView(generic.CreateView):
    model = models.Deportes
    form_class = DeporteForm
    template_name = 'deportes_create.html'
    success_url = reverse_lazy('torre_crud:deportes-list') 

class DeportesDeleteView(generic.DeleteView):
    model = models.Deportes
    template_name = 'deportes_confirm_delete.html'
    success_url = reverse_lazy('torre_crud:deportes-list')

class DeportesUpdateView(generic.UpdateView):
    model = models.Deportes
    form_class = DeporteForm
    template_name = 'deportes_update.html'
    success_url = reverse_lazy('torre_crud:deportes-list')

""" Instalaciones """

class InstalacionesListView(generic.ListView):
    template_name = 'instalaciones_list.html'
    context_object_name = 'instalaciones'

    def get_queryset(self):
        return models.Instalaciones.objects.all()

class InstalacionesCreateView(generic.CreateView):
    model = models.Instalaciones
    form_class = InstalacionForm
    template_name = 'instalaciones_create.html'
    success_url = reverse_lazy('torre_crud:instalaciones-list')

class InstalacionesDeleteView(generic.DeleteView):
    model = models.Instalaciones
    template_name = 'instalaciones_delete.html'
    success_url = reverse_lazy('torre_crud:instalaciones-list')

class InstalacionesUpdateView(generic.UpdateView):
    model = models.Instalaciones
    form_class = InstalacionForm
    template_name = 'instalaciones_update.html'
    success_url = reverse_lazy('torre_crud:instalaciones-list')

""" Equipo """

class EquiposListView(generic.ListView):
    template_name = 'equipos_list.html'
    context_object_name = 'equipos_list'

    def get_queryset(self):
        return models.Equipos.objects.all()

class EquiposCreateView(generic.CreateView):
    model = models.Equipos
    form_class = EquipoForm
    template_name = 'equipo_create.html'
    success_url = reverse_lazy('torre_crud:equipos-list')

class EquiposDeleteView(generic.DeleteView):
    model = models.Equipos
    template_name = 'equipo_confirm_delete.html'
    success_url = reverse_lazy('torre_crud:equipos-list')

class EquiposUpdateView(generic.UpdateView):
    model = models.Equipos
    form_class = EquipoForm
    template_name = 'equipo_update.html'
    success_url = reverse_lazy('torre_crud:equipos-list')

class EquipoDetailView(generic.DetailView):
    model = models.Equipos
    template_name = 'equipo_detail.html'
    context_object_name = 'equipo'

    def get_queryset(self):
        return super().get_queryset()
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        equipo = self.get_object()
        jugadores = models.Jugadores.objects.filter(id_equipo=equipo)
        contexto['jugadores'] = jugadores
        return contexto
    

class EquipoJugadorCreate(generic.CreateView):
    model = models.Jugadores
    form_class = JugadorForm
    template_name = 'equipo_jugador_create.html'
    success_url = reverse_lazy('torre_crud:equipos-list')  # Esta es la URL a la que se redirigirá después de crear el jugador

    def get_initial(self):
        initial = super().get_initial()
        equipo_id = self.kwargs.get('pk')
        equipo = models.Equipos.objects.get(pk=equipo_id)
        initial['equipo'] = equipo
        return initial

""" Jugador """

class JugadorListView(generic.ListView):
    model = models.Jugadores
    template_name = 'jugadores_list.html'
    context_object_name = 'jugadores'
    

class JugadorCreateView(generic.CreateView):
    model = models.Jugadores
    form_class = JugadorForm
    success_url = reverse_lazy('torre_crud:jugadores-list') 
    template_name = 'jugador_create.html'

class JugadorUpdateView(generic.UpdateView):
    model = models.Jugadores
    form_class = JugadorForm
    success_url = reverse_lazy('torre_crud:jugadores-list') 
    template_name = 'jugador_update.html'

class JugadorDetailView(generic.DetailView):
    model = models.Jugadores
    template_name = 'jugador_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        jugador = self.get_object()
        context['equipo'] = jugador.id_equipo.nombre
        context['elJugador'] = jugador
        return context

class JugadorDeleteView(generic.DeleteView):
    model = models.Jugadores
    success_url = reverse_lazy('torre_crud:jugadores-list')  
    template_name = 'jugador_confirm_delete.html'

""" Partidos """

class PartidoListView(generic.ListView):
    model = models.Partidos
    template_name = 'partido_list.html'
    context_object_name = 'partidos'
    ordering = ['-fecha_hora']

class PartidoCreateView(generic.CreateView):
    model = models.Partidos
    form_class = PartidoForm
    success_url = reverse_lazy('torre_crud:partidos-list') 
    template_name = 'partido_create.html'

class PartidoUpdateView(generic.UpdateView):
    model = models.Partidos
    form_class = PartidoForm
    success_url = reverse_lazy('torre_crud:partidos-list') 
    template_name = 'partido_update.html'

class PartidoDetailView(generic.DetailView):
    model = models.Partidos
    template_name = 'partido_detail.html'
    context_object_name = 'partido'

class PartidoDeleteView(generic.DeleteView):
    model = models.Partidos
    success_url = reverse_lazy('torre_crud:partidos-list')
    template_name = 'partido_confirm_delete.html'
