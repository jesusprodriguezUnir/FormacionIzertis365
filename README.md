# Portal Educativo - Guía de Instalación y Uso

## Requisitos Previos

- Python 3.9 o superior
- pip (gestor de paquetes de Python)
- Git (opcional)

## Instalación

### 1. Clonar o descargar el proyecto

```bash
cd aplicacion_web
```

### 2. Crear un entorno virtual (recomendado)

**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configuración del proyecto

Copia el archivo `.env.example` a `.env` y configura las variables necesarias:

```bash
copy .env.example .env
```

Edita el archivo `.env` con tus valores:

```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear un superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario administrador.

### 7. Cargar datos iniciales

```bash
python manage.py load_initial_data
```

Este comando cargará automáticamente:
- 4 secciones de formación (Tema 1-4)
- 12 recursos educativos
- Configuración inicial del portal

### 8. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

¡El portal está listo! Accede a:
- **Portal:** http://localhost:8000
- **Admin:** http://localhost:8000/admin

## Uso

### Navegación

- **Inicio:** Página principal con recursos destacados
- **Secciones:** Catálogo completo de temas de formación
- **Búsqueda:** Busca recursos por título o contenido
- **Admin:** Panel de administración para gestionar contenido

### Gestión de Contenido (Panel Admin)

En http://localhost:8000/admin puedes:

1. **Crear Secciones**
   - Añadir nuevos temas
   - Cargar imágenes
   - Definir orden de aparición

2. **Crear Recursos**
   - Enlazar a recursos externos
   - Cargar documentos
   - Establecer dificultad y duración
   - Añadir thumbnails

3. **Crear Documentos**
   - Vincular documentos a recursos
   - Clasificar por tipo (normativa, guía, manual, etc.)

## Estructura del Proyecto

```
aplicacion_web/
├── manage.py                      # Utilidad de gestión de Django
├── requirements.txt               # Dependencias de Python
├── .env.example                   # Ejemplo de variables de entorno
├── .gitignore                     # Archivos ignorados por git
├── db.sqlite3                     # Base de datos (se crea automáticamente)
│
├── portal_educativo/              # Configuración principal del proyecto
│   ├── settings.py                # Configuración de Django
│   ├── urls.py                    # URLs principales
│   ├── wsgi.py                    # Configuración WSGI
│   ├── asgi.py                    # Configuración ASGI
│   └── static/                    # Archivos estáticos (CSS, JS)
│
├── core/                          # Aplicación principal
│   ├── models.py                  # Modelos de datos (Section, Resource, Document)
│   ├── views.py                   # Vistas (lógica de negocio)
│   ├── urls.py                    # URLs de la aplicación
│   ├── admin.py                   # Configuración del panel admin
│   ├── apps.py                    # Configuración de la aplicación
│   │
│   ├── templates/core/            # Plantillas HTML
│   │   ├── base.html              # Plantilla base (header, footer, estilos)
│   │   ├── index.html             # Página principal
│   │   ├── section_list.html      # Lista de secciones
│   │   ├── section_detail.html    # Detalle de sección
│   │   ├── resource_detail.html   # Detalle de recurso
│   │   └── search.html            # Página de búsqueda
│   │
│   ├── static/css/                # Estilos CSS personalizados
│   ├── static/js/                 # Scripts JavaScript
│   │
│   └── management/commands/       # Comandos personalizados
│       └── load_initial_data.py   # Carga datos iniciales
│
└── media/                         # Archivos subidos por el usuario
    ├── documentos/                # Documentos educativos
    └── recursos/                  # Otros recursos
```

## Características Principales

### 🎨 Diseño Responsive
- Interfaz adaptable a dispositivos móviles y desktop
- Uso de Bootstrap 5 para estilización moderna
- Gradientes y animaciones suaves

### 🔍 Búsqueda Avanzada
- Búsqueda en tiempo real
- Búsqueda por título y descripción
- Resultados organizados por tipo (secciones, recursos, documentos)

### 📚 Gestión de Contenido
- Panel administrativo completo
- Carga de imágenes y documentos
- Ordenamiento personalizado de recursos

### 🏷️ Categorización
- Secciones temáticas
- Tipos de recursos (enlace, documento, video, imagen, ejercicio, herramienta)
- Niveles de dificultad (básico, intermedio, avanzado)
- Duración estimada por recurso

### 🔐 Seguridad
- Protección CSRF
- Validación de entrada
- Variables de entorno para datos sensibles

## Solución de Problemas

### El servidor no inicia
```
Error: "No module named 'django'"
Solución: pip install -r requirements.txt
```

### Base de datos no inicializada
```
Error: "no such table"
Solución: python manage.py migrate
```

### Datos de ejemplo no se cargan
```
Solución: python manage.py load_initial_data
```

### Puerto 8000 en uso
```
Solución: python manage.py runserver 8001
```

## Desarrollo Futuro

Posibles mejoras:
1. Integración con Microsoft Graph API para leer datos de SharePoint
2. Sistema de usuarios con registro y login
3. Seguimiento de progreso de aprendizaje
4. Sistema de calificaciones y certificados
5. Notificaciones por email
6. API REST para integración externa
7. Soporte para múltiples idiomas

## Contacto y Soporte

Para preguntas o soporte, contacta a:
- Formación Izertis 2026
- Casa Rural El Olivo

---

**Versión:** 1.0
**Fecha:** Enero 2026
**Licencia:** Todos los derechos reservados © 2026
