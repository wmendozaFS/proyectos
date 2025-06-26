from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Proyecto
from .forms import ProyectoForm
from django.urls import reverse_lazy

def landing(request):
    return render(request, 'landing.html')

class ProyectoListView(ListView):
    model = Proyecto
    template_name = 'proyectos/lista.html'

class ProyectoCreateView(CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/form.html'
    success_url = reverse_lazy('lista')

class ProyectoUpdateView(UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'proyectos/form.html'
    success_url = reverse_lazy('lista')

def form_valid(self, form):
    form.instance.usuario = self.request.user
    return super().form_valid(form)
