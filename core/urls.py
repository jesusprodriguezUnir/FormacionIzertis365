from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Página principal
    path('', views.IndexView.as_view(), name='index'),
    
    # Secciones
    path('secciones/', views.SectionListView.as_view(), name='section_list'),
    path('seccion/<slug:slug>/', views.SectionDetailView.as_view(), name='section_detail'),
    
    # Recursos
    path('recurso/<slug:slug>/', views.ResourceDetailView.as_view(), name='resource_detail'),
    path('recurso/<slug:slug>/slides/', views.SlideListView.as_view(), name='slide_list'),
    
    # Búsqueda
    path('buscar/', views.SearchView.as_view(), name='search'),
]
