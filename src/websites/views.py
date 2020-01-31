from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import WebsiteForm
from .models import Website


class WebsiteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'websites/create.html'
    form_class = WebsiteForm


class WebsiteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'websites/detail.html'
    model = Website


class WebsiteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'websites/update.html'
    form_class = WebsiteForm
    queryset = Website.objects.all()


class WebsiteListView(LoginRequiredMixin, ListView):
    template_name = 'websites/list.html'
    model = Website


class WebsiteDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'websites/delete.html'
    model = Website
    success_url = reverse_lazy('websites:list')
