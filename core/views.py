from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import get_object_or_404
from .models import Section, Resource, Document, Slide


class IndexView(TemplateView):
    """Vista principal del portal."""
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = Section.objects.filter(is_active=True)
        context['featured_resources'] = Resource.objects.filter(
            is_active=True
        ).select_related('section')[:6]
        return context


class SectionListView(ListView):
    """Lista todas las secciones."""
    model = Section
    template_name = 'core/section_list.html'
    context_object_name = 'sections'
    paginate_by = 12

    def get_queryset(self):
        return Section.objects.filter(is_active=True)


class SectionDetailView(DetailView):
    """Detalle de una sección con sus recursos."""
    model = Section
    template_name = 'core/section_detail.html'
    context_object_name = 'section'
    slug_field = 'slug'

    def get_queryset(self):
        return Section.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resources'] = self.object.resources.filter(is_active=True)
        return context


class ResourceDetailView(DetailView):
    """Detalle de un recurso."""
    model = Resource
    template_name = 'core/resource_detail.html'
    context_object_name = 'resource'
    slug_field = 'slug'

    def get_queryset(self):
        return Resource.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = self.object.documents.filter(is_active=True)
        context['slides'] = self.object.slides.all().order_by('slide_number')
        context['slides_count'] = context['slides'].count()
        context['related_resources'] = Resource.objects.filter(
            section=self.object.section,
            is_active=True
        ).exclude(id=self.object.id)[:5]
        return context


class SearchView(TemplateView):
    """Vista de búsqueda."""
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        
        if query:
            context['query'] = query
            context['sections'] = Section.objects.filter(
                is_active=True,
                title__icontains=query
            ) | Section.objects.filter(
                is_active=True,
                description__icontains=query
            )
            context['resources'] = Resource.objects.filter(
                is_active=True,
                title__icontains=query
            ) | Resource.objects.filter(
                is_active=True,
                description__icontains=query
            )
            context['documents'] = Document.objects.filter(
                is_active=True,
                title__icontains=query
            )
        
        return context


class SlideListView(DetailView):
    """Vista para mostrar todos los slides de un recurso con navegación."""
    model = Resource
    template_name = 'core/slide_list.html'
    context_object_name = 'resource'
    slug_field = 'slug'

    def get_queryset(self):
        return Resource.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = self.object.slides.all().order_by('slide_number')
        context['slides_count'] = context['slides'].count()
        
        # Para navegación anterior/siguiente
        current_slide_num = int(self.request.GET.get('slide', 1))
        context['current_slide_number'] = current_slide_num
        
        if context['slides_count'] > 0:
            context['current_slide'] = context['slides'].filter(slide_number=current_slide_num).first()
            if not context['current_slide']:
                context['current_slide'] = context['slides'].first()
                context['current_slide_number'] = context['current_slide'].slide_number
        
        return context
