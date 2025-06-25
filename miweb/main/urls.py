from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('proyectos/nuevo/', views.ProyectoCreateView.as_view(), name='nuevo'),
    path('proyectos/editar/', views.ProyectoUpdateView.as_view(), name='editar'),
    path('proyectos/lista', views.ProyectoListView.as_view(), name='lista'),
]