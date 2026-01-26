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
                'description': 'Guía completa de bienvenida para huéspedes. Incluye instrucciones de uso, normas y servicios disponibles.',
                'resource_type': 'document',
                'section': sections['tema-1-copilot-app'],
                'duration': '15 min',
                'difficulty': 'basico',
                'order': 1,
            },
            {
                'title': 'Cuadernos de Formación',
                'description': 'Material educativo interactivo. Cuadernos con bases de conocimiento sobre normativa de casas rurales.',
                'resource_type': 'document',
                'section': sections['tema-1-copilot-app'],
                'duration': '30 min',
                'difficulty': 'intermedio',
                'order': 2,
            },
            {
                'title': 'Diseño con Designer',
                'description': 'Crea imágenes profesionales usando Designer. Generación de logos, banners y materiales visuales.',
                'resource_type': 'exercise',
                'section': sections['tema-1-copilot-app'],
                'duration': '45 min',
                'difficulty': 'intermedio',
                'order': 3,
            },
            {
                'title': 'Agente Inteligente - Casa Rural',
                'description': 'Configura un agente IA para atender a huéspedes. Gestiona consultas y reservas automáticamente.',
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
                'description': 'Crea libros de Excel con Copilot para control de ingresos y gastos de tu negocio.',
                'resource_type': 'document',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '30 min',
                'difficulty': 'basico',
                'order': 1,
            },
            {
                'title': 'Formularios con Forms',
                'description': 'Diseña formularios de reserva y consultas usando Microsoft Forms integrado con Copilot.',
                'resource_type': 'tool',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '20 min',
                'difficulty': 'basico',
                'order': 2,
            },
            {
                'title': 'Presentaciones en PowerPoint',
                'description': 'Genera presentaciones profesionales con Copilot. Material promocional y comercial.',
                'resource_type': 'document',
                'section': sections['tema-2-copilot-herramientas'],
                'duration': '40 min',
                'difficulty': 'intermedio',
                'order': 3,
            },
            {
                'title': 'Documentos en Word',
                'description': 'Redacta contenido profesional con Copilot. Cartas, contratos y documentación empresarial.',
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
                'title': 'Automatización de Procesos',
                'description': 'Crea flujos de trabajo automáticos para optimizar tu negocio. Integración con aplicaciones Microsoft.',
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
                'title': 'Agente de Clasificación de Incidencias',
                'description': 'Crea un agente que clasifique automáticamente incidencias en categorías. Material, Limpieza, Mantenimiento, Urgencia Grave.',
                'resource_type': 'tool',
                'section': sections['tema-4-copilot-studio'],
                'duration': '45 min',
                'difficulty': 'avanzado',
                'order': 1,
            },
            {
                'title': 'Configuración del Agente',
                'description': 'Aprende a configurar y personalizar agentes en Copilot Studio. Instrucciones y mejores prácticas.',
                'resource_type': 'document',
                'section': sections['tema-4-copilot-studio'],
                'duration': '30 min',
                'difficulty': 'intermedio',
                'order': 2,
            },
            {
                'title': 'Base de Conocimiento (RAG)',
                'description': 'Integra documentos y manuales en tu agente. Sistema de Recuperación Aumentada por Generación.',
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
