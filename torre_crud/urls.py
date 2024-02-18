from django.urls import path
from . import views
app_name = 'torre_crud'

urlpatterns = [
    path('', views.Inicio.as_view(), name='inicio'),

    # URLs para Deportes
    path('deportes/', views.DeportesListView.as_view(), name='deportes-list'),
    path('deportes/create/', views.DeportesCreateView.as_view(), name='deportes-create'),
    path('deportes/<int:pk>/update/', views.DeportesUpdateView.as_view(), name='deportes-update'),
    path('deportes/<int:pk>/delete/', views.DeportesDeleteView.as_view(), name='deportes-delete'),

    # URLs para Instalaciones
    path('instalaciones/', views.InstalacionesListView.as_view(), name='instalaciones-list'),
    path('instalaciones/create/', views.InstalacionesCreateView.as_view(), name='instalaciones-create'),
    path('instalaciones/<int:pk>/update/', views.InstalacionesUpdateView.as_view(), name='instalaciones-update'),
    path('instalaciones/<int:pk>/delete/', views.InstalacionesDeleteView.as_view(), name='instalaciones-delete'),

    # URLs para Equipos
    path('equipos/', views.EquiposListView.as_view(), name='equipos-list'),
    path('equipos/create/', views.EquiposCreateView.as_view(), name='equipos-create'),
    path('equipos/<int:pk>/update/', views.EquiposUpdateView.as_view(), name='equipos-update'),
    path('equipos/<int:pk>/delete/', views.EquiposDeleteView.as_view(), name='equipos-delete'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo-detail'),

    # URLs para Jugadores
    path('jugadores/', views.JugadorListView.as_view(), name='jugadores-list'),
    path('jugadores/create/', views.JugadorCreateView.as_view(), name='jugadores-create'),
    path('jugadores/<int:pk>/update/', views.JugadorUpdateView.as_view(), name='jugadores-update'),
    path('jugadores/<int:pk>/delete/', views.JugadorDeleteView.as_view(), name='jugadores-delete'),
    path('jugadores/<int:pk>/', views.JugadorDetailView.as_view(), name='jugador-detail'),

    # URLs para Partidos
    path('partidos/', views.PartidoListView.as_view(), name='partidos-list'),
    path('partidos/create/', views.PartidoCreateView.as_view(), name='partidos-create'),
    path('partidos/<int:pk>/update/', views.PartidoUpdateView.as_view(), name='partidos-update'),
    path('partidos/<int:pk>/delete/', views.PartidoDeleteView.as_view(), name='partidos-delete'),
    path('partidos/<int:pk>/', views.PartidoDetailView.as_view(), name='partido-detail'),
]