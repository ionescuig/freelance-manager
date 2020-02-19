from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import ProjectForm
from .models import Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/create.html'
    form_class = ProjectForm

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data()
        context['linkActive'] = 'Projects'
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'projects/detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data()
        context['linkActive'] = 'Projects'
        return context


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'projects/update.html'
    form_class = ProjectForm
    queryset = Project.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProjectUpdateView, self).get_context_data()
        context['linkActive'] = 'Projects'
        return context


class ProjectListView(LoginRequiredMixin, ListView):
    template_name = 'projects/list.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data()
        context['linkActive'] = 'Projects'
        return context


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'projects/delete.html'
    model = Project
    success_url = reverse_lazy('projects:list')

    def get_context_data(self, **kwargs):
        context = super(ProjectDeleteView, self).get_context_data()
        context['linkActive'] = 'Projects'
        return context
