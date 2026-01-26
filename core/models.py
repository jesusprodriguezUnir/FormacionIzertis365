from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Section(models.Model):
    """Representa una sección/tema del portal educativo."""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default='folder', help_text='Nombre del icono Bootstrap')
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to='secciones/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Resource(models.Model):
    """Representa un recurso educativo (enlace, documento, etc)."""
    RESOURCE_TYPES = (
        ('link', 'Enlace Externo'),
        ('document', 'Documento'),
        ('video', 'Video'),
        ('image', 'Imagen'),
        ('exercise', 'Ejercicio'),
        ('tool', 'Herramienta'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES, default='link')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='resources')
    url = models.URLField(blank=True, null=True, help_text='URL del recurso externo')
    document = models.FileField(upload_to='documentos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    duration = models.CharField(max_length=50, blank=True, help_text='Ej: 30 min, 1 hora')
    difficulty = models.CharField(
        max_length=20,
        choices=[('basico', 'Básico'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')],
        default='basico'
    )

    class Meta:
        ordering = ['section', 'order', 'title']
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return f"{self.title} ({self.section.title})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Document(models.Model):
    """Representa documentos normativa y referencias."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True)
    document_type = models.CharField(
        max_length=50,
        choices=[
            ('normativa', 'Normativa'),
            ('guia', 'Guía'),
            ('manual', 'Manual'),
            ('plantilla', 'Plantilla'),
            ('referencia', 'Referencia'),
        ],
        default='referencia'
    )
    file = models.FileField(upload_to='documentos/normativos/')
    resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, blank=True, null=True, related_name='documents')
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
