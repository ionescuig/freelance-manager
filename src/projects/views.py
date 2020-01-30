from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import ProjectForm
from .models import Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create.html'
    form_class = ProjectForm


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/detail.html'
    model = Project


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/update.html'
    form_class = ProjectForm
    queryset = Project.objects.all()


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'projects/list.html'
    model = Project


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/delete.html'
    model = Project
    success_url = reverse_lazy('projects:list')
