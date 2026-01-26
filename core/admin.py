from django.contrib import admin
from .models import Section, Resource, Document, Slide


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('order', 'title')
    fieldsets = (
        ('Información Básica', {'fields': ('title', 'slug', 'description')}),
        ('Presentación', {'fields': ('icon', 'image')}),
        ('Configuración', {'fields': ('order', 'is_active')}),
    )


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'resource_type', 'difficulty', 'is_active', 'created_at')
    list_filter = ('resource_type', 'difficulty', 'is_active', 'section', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Información Básica', {'fields': ('title', 'slug', 'section', 'description')}),
        ('Tipo de Recurso', {'fields': ('resource_type', 'url', 'document')}),
        ('Metadatos', {'fields': ('duration', 'difficulty', 'order')}),
        ('Visualización', {'fields': ('thumbnail',)}),
        ('Configuración', {'fields': ('is_active',)}),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'resource', 'is_active', 'created_at')
    list_filter = ('document_type', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Información Básica', {'fields': ('title', 'slug', 'description')}),
        ('Tipo de Documento', {'fields': ('document_type', 'file')}),
        ('Relación', {'fields': ('resource',)}),
        ('Configuración', {'fields': ('order', 'is_active')}),
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('slide_number', 'title_truncated', 'resource', 'created_at')
    list_filter = ('resource', 'created_at')
    search_fields = ('title', 'content', 'resource__title')
    ordering = ('resource', 'slide_number')
    fieldsets = (
        ('Información Básica', {'fields': ('resource', 'slide_number', 'title')}),
        ('Contenido', {'fields': ('content', 'notes')}),
        ('Imagen', {'fields': ('image',)}),
        ('Configuración', {'fields': ('order',)}),
    )
    readonly_fields = ('created_at', 'updated_at')
    
    def title_truncated(self, obj):
        """Muestra el título truncado en el listado."""
        if obj.title:
            return obj.title[:50] + '...' if len(obj.title) > 50 else obj.title
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    title_truncated.short_description = 'Título/Contenido'
