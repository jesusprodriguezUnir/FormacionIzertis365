"""
Script para cargar datos iniciales desde los archivos del workspace
"""
import json
import os
from pathlib import Path
from django.core.management.base import BaseCommand
from core.models import Section, Resource, Document


class Command(BaseCommand):
    help = 'Carga datos iniciales del workspace de Izertis'

    def handle(self, *args, **options):
        self.stdout.write("Iniciando carga de datos...")
        
        # Crear secciones
        sections_data = [
            {
                'title': 'Tema 1 - Copilot App',
                'slug': 'tema-1-copilot-app',
                'description': 'Aprende a utilizar Copilot App para crear contenido innovador. Incluyendo guías de usuario, cuadernos, diseño y agentes inteligentes.',
                'icon': 'bi-laptop',
                'order': 1,
            },
            {
                'title': 'Tema 2 - Copilot en Herramientas',
                'slug': 'tema-2-copilot-herramientas',
                'description': 'Integración de Copilot en herramientas Microsoft 365: Excel, Word, PowerPoint y Forms.',
                'icon': 'bi-tools',
                'order': 2,
            },
            {
                'title': 'Tema 3 - Power Automate',
                'slug': 'tema-3-power-automate',
                'description': 'Automatiza procesos empresariales con Power Automate. Crea flujos de trabajo eficientes.',
                'icon': 'bi-lightning',
                'order': 3,
            },
            {
                'title': 'Tema 4 - Copilot Studio',
                'slug': 'tema-4-copilot-studio',
                'description': 'Crea agentes IA personalizados con Copilot Studio. Automatiza interacciones con clientes.',
                'icon': 'bi-robot',
                'order': 4,
            },
        ]
        
        sections = {}
        for section_data in sections_data:
            section, created = Section.objects.get_or_create(
                slug=section_data['slug'],
                defaults=section_data
            )
            sections[section_data['slug']] = section
            status = "creada" if created else "existente"
            self.stdout.write(self.style.SUCCESS(f"✓ Sección '{section.title}' {status}"))

        # Crear recursos para Tema 1
        resources_data_tema1 = [
            {
                'title': 'Guía de Usuario - Casa Rural El Olivo',
                'description': 'Guía completa de bienvenida para huéspedes: presentación de propiedad, instrucciones de acceso y seguridad, servicios disponibles (Wi-Fi, cocina, piscina), normas de convivencia, ubicación y atractivos cercanos. Creada con Copilot para tono profesional.',
                'resource_type': 'document',
                'section': sections['tema-1-copilot-app'],
                'duration': '15 min',
                'difficulty': 'basico',
                'order': 1,
            },
            {
                'title': 'Cuadernos de Formación - Normativa de Casas Rurales',
                'description': 'Material educativo interactivo con base de conocimiento sobre regulación. Contiene marco legal, seguridad, higiene, derechos del propietario, protección del consumidor. Incluye referencias normativas: BOCM, BOE, Normativa Regional. Acceso a documentos normativos originales, explicaciones simplificadas y ejemplos prácticos.',
                'resource_type': 'document',
                'section': sections['tema-1-copilot-app'],
                'duration': '30 min',
                'difficulty': 'intermedio',
                'order': 2,
            },
            {
                'title': 'Diseño con Designer - Creación de Materiales Visuales',
                'description': 'Aprende a generar imágenes profesionales con Microsoft Designer + Copilot. Ejercicios: logos minimalistas, banners promocionales, imágenes de interiores/exteriores, materiales marketing. Competencias: prompts descriptivos, edición de imágenes, optimización por plataforma, marca visual consistente. Resultados: 3-5 diseños listos para publicar.',
                'resource_type': 'exercise',
                'section': sections['tema-1-copilot-app'],
                'duration': '45 min',
                'difficulty': 'intermedio',
                'order': 3,
            },
            {
                'title': 'Agente Inteligente - Atención al Cliente con IA',
                'description': 'Configuración de agente Copilot Studio personalizado. Funcionalidades: consultas disponibilidad, info servicios, asistencia reservas, consultas ubicación/actividades, gestión incidencias, horarios check-in/out. Integración con calendario, base conocimiento, análisis sentimiento, escalado a humanos. Casos uso: atención 24/7, reducción carga admin, experiencia personalizada.',
                'resource_type': 'tool',
                'section': sections['tema-1-copilot-app'],
                'duration': '60 min',
                'difficulty': 'avanzado',
                'order': 4,
            },
        ]
        
        for resource_data in resources_data_tema1:
            resource, created = Resource.objects.get_or_create(
                title=resource_data['title'],
                section=resource_data['section'],
                defaults=resource_data
            )
            status = "creado" if created else "existente"
            self.stdout.write(self.style.SUCCESS(f"✓ Recurso '{resource.title}' {status}"))

        # Crear recursos para Tema 2
        resources_data_tema2 = [
            {
                'title': 'Control Financiero en Excel',
                'description': 'Crea libros Excel con Copilot para gestión financiera. Incluye: tablas ingresos/gastos, gráficos visualización, cálculos automáticos, análisis mensual/trimestral, presupuestos, reportes. Competencias: fórmulas avanzadas, tablas dinámicas, gráficos interpretativos, análisis de datos. Resultados: dashboard financiero funcional para Casa Rural.',
                'resource_type': 'document',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '30 min',
                'difficulty': 'basico',
                'order': 1,
            },
            {
                'title': 'Formularios con Forms - Reservas y Encuestas',
                'description': 'Diseña formularios profesionales con Microsoft Forms + Copilot. Tipos: formulario reserva con fechas/huéspedes, encuesta satisfacción post-estancia, consulta de servicios adicionales. Análisis de respuestas automático, integración con Excel, reportes visuales. Competencias: diseño UX, validaciones, ramificación lógica.',
                'resource_type': 'tool',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '20 min',
                'difficulty': 'basico',
                'order': 2,
            },
            {
                'title': 'Presentaciones en PowerPoint - Promoción Turística',
                'description': 'Genera presentaciones profesionales 6-8 diapositivas para promocionar Casa Rural. Estructura: Descripción propuesta única, Servicios/comodidades destacados, Ubicación/atractivos turísticos, Experiencias/actividades locales, Cómo reservar + CTA. Tono persuasivo orientado turismo. Imágenes paisajes, interiores acogedores, actividades. Resultados: material promocional listo para agencias turismo.',
                'resource_type': 'document',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '40 min',
                'difficulty': 'intermedio',
                'order': 3,
            },
            {
                'title': 'Documentos en Word - Comunicaciones Profesionales',
                'description': 'Redacta contenido profesional con Copilot en Word. Tipos documentos: confirmaciones reserva, términos & condiciones, políticas cancelación, cartas a huéspedes, contratos de servicios, newsletters, informes. Competencias: tono profesional, estructura clara, formateo avanzado, generación de firmas digitales.',
                'resource_type': 'document',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '25 min',
                'difficulty': 'basico',
                'order': 4,
            },
        ]
        
        for resource_data in resources_data_tema2:
            resource, created = Resource.objects.get_or_create(
                title=resource_data['title'],
                section=resource_data['section'],
                defaults=resource_data
            )
            status = "creado" if created else "existente"
            self.stdout.write(self.style.SUCCESS(f"✓ Recurso '{resource.title}' {status}"))

        # Crear recursos para Tema 3
        resources_data_tema3 = [
            {
                'title': 'Automatización de Procesos con Power Automate',
                'description': 'Crea flujos de trabajo automáticos para optimizar operaciones Casa Rural. Flujos: solicitud reserva → confirmación email automática, nuevo huésped → envío guía bienvenida, check-out → envío encuesta satisfacción, incidencia → ticket soporte, pago recibido → factura automática. Integraciones: Excel, Outlook, SharePoint, Teams. Competencias: triggers, acciones condicionales, variables, loop handling.',
                'resource_type': 'exercise',
                'section': sections['tema-3-power-automate'],
                'duration': '50 min',
                'difficulty': 'avanzado',
                'order': 1,
            },
        ]
        
        for resource_data in resources_data_tema3:
            resource, created = Resource.objects.get_or_create(
                title=resource_data['title'],
                section=resource_data['section'],
                defaults=resource_data
            )
            status = "creado" if created else "existente"
            self.stdout.write(self.style.SUCCESS(f"✓ Recurso '{resource.title}' {status}"))

        # Crear recursos para Tema 4
        resources_data_tema4 = [
            {
                'title': 'Agente de Clasificación de Incidencias - Mantenimiento',
                'description': 'Crea agente Copilot Studio que clasifique automáticamente incidencias reportadas. Categorías: Material (enseres/equipamiento), Limpieza (sábanas/baños), Mantenimiento (tuberías/electricidad), Urgencia Grave (seguridad/salud). Análisis automático, asignación a técnicos, notificaciones. Machine Learning aprende patrones incidencias. Resultados: reducción 70% tiempo triage, mejor priorización urgencias.',
                'resource_type': 'tool',
                'section': sections['tema-4-copilot-studio'],
                'duration': '45 min',
                'difficulty': 'avanzado',
                'order': 1,
            },
            {
                'title': 'Configuración del Agente',
                'description': 'Configura parámetros del agente Copilot Studio: Instrucciones del sistema (rol/tono/contexto). Modelos de lenguaje (GPT-4/3.5). Fuentes de datos (SharePoint/Excel/Teams). Personas (roles específicos). Acciones de escalada (criterios/destinos). Pruebas de conversación (casos uso). Análisis de logs y feedback usuario. Competencias: prompts avanzados, flujos condicionales, integración datos, monitoreo performance.',
                'resource_type': 'document',
                'section': sections['tema-4-copilot-studio'],
                'duration': '30 min',
                'difficulty': 'avanzado',
                'order': 2,
            },
            {
                'title': 'Base de Conocimiento (RAG)',
                'description': 'Integra Base de Conocimiento RAG (Retrieval-Augmented Generation) en agente Copilot Studio. Conecta múltiples fuentes: manuales PDF, políticas Word, normativas Excel, FAQs SharePoint, wikis internas. Sistema busca contexto relevante automáticamente. Casos uso: soporte técnico contextualizado, normativa legal actualizada, procedimientos operacionales. Configuración: indexación documentos, relevancia búsqueda, actualización periódica. Competencias: gestión documental, búsqueda semántica, análisis relevancia.',
                'resource_type': 'document',
                'section': sections['tema-4-copilot-studio'],
                'duration': '35 min',
                'difficulty': 'avanzado',
                'order': 3,
            },
        ]
        
        for resource_data in resources_data_tema4:
            resource, created = Resource.objects.get_or_create(
                title=resource_data['title'],
                section=resource_data['section'],
                defaults=resource_data
            )
            status = "creado" if created else "existente"
            self.stdout.write(self.style.SUCCESS(f"✓ Recurso '{resource.title}' {status}"))

        self.stdout.write(self.style.SUCCESS('\n✓ Datos cargados correctamente'))
