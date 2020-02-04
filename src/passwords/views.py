from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import PasswordForm
from .models import Password


class PasswordCreateView(LoginRequiredMixin, CreateView):
    template_name = 'passwords/create.html'
    form_class = PasswordForm


class PasswordDetailView(LoginRequiredMixin, DetailView):
    template_name = 'passwords/detail.html'
    model = Password


class PasswordUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'passwords/update.html'
    form_class = PasswordForm
    queryset = Password.objects.all()


class PasswordListView(LoginRequiredMixin, ListView):
    template_name = 'passwords/list.html'
    model = Password


class ProjectPasswordsListView(LoginRequiredMixin, ListView):
    """
    Passwords for a specific project.
    """
    template_name = 'passwords/list.html'
    model = Password

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Password.objects.filter(project_id=pk)


class PasswordDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'passwords/delete.html'
    model = Password
    success_url = reverse_lazy('passwords:list')
