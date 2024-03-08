# Proyecto Torre CRUD

Este es un proyecto Django para gestionar deportes, equipos, instalaciones, jugadores y partidos. Permite realizar operaciones básicas de creación, lectura, actualización y eliminación (CRUD) sobre estos elementos.

## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

- **torre_crud/**: Directorio principal del proyecto Django.
  - **static/**: Carpeta que contiene archivos estáticos como hojas de estilo CSS e imágenes.
    - **css/**: Carpeta que contiene archivos CSS.
      - **base.css**: Archivo CSS principal con estilos base para la aplicación.
    - **img/**: Carpeta que contiene imágenes utilizadas en la aplicación.
  - **templates/**: Carpeta que contiene las plantillas HTML utilizadas en las vistas.
  - **admin.py**: Archivo donde se registran los modelos para la interfaz de administración de Django.
  - **apps.py**: Archivo de configuración de la aplicación Django.
  - **forms.py**: Archivo que define los formularios utilizados en la aplicación.
  - **models.py**: Archivo que define los modelos de datos utilizados en la aplicación.
  - **urls.py**: Archivo de configuración de las URLs de la aplicación.
  - **views.py**: Archivo que contiene las vistas de las páginas web.

### Funcionalidades Principales

- **Gestión de Deportes**: Permite agregar, editar y eliminar deportes.
- **Gestión de Instalaciones**: Permite agregar, editar y eliminar instalaciones deportivas.
- **Gestión de Equipos**: Permite agregar, editar y eliminar equipos, así como asignar jugadores a equipos.
- **Gestión de Jugadores**: Permite agregar, editar y eliminar jugadores, así como ver detalles de cada jugador.
- **Gestión de Partidos**: Permite agregar, editar y eliminar partidos, así como ver detalles de cada partido.

## Autores

- [Francisco Javier Martín-Lunas Escobar](https://github.com/xavivi8) - Desarrollador principal

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE.md](LICENSE) para más detalles.
