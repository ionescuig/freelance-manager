from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import WebsiteForm
from .models import Website


class WebsiteCreateView(LoginRequiredMixin, CreateView):
    template_name = 'websites/create.html'
    form_class = WebsiteForm

    def get_context_data(self, **kwargs):
        context = super(WebsiteCreateView, self).get_context_data()
        context['linkActive'] = 'Websites'
        return context


class WebsiteDetailView(LoginRequiredMixin, DetailView):
    template_name = 'websites/detail.html'
    model = Website

    def get_context_data(self, **kwargs):
        context = super(WebsiteDetailView, self).get_context_data()
        context['linkActive'] = 'Websites'
        return context


class WebsiteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'websites/update.html'
    form_class = WebsiteForm
    queryset = Website.objects.all()

    def get_context_data(self, **kwargs):
        context = super(WebsiteUpdateView, self).get_context_data()
        context['linkActive'] = 'Websites'
        return context


class WebsiteListView(LoginRequiredMixin, ListView):
    template_name = 'websites/list.html'
    model = Website

    def get_context_data(self, **kwargs):
        context = super(WebsiteListView, self).get_context_data()
        context['linkActive'] = 'Websites'
        return context


class WebsiteDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'websites/delete.html'
    model = Website
    success_url = reverse_lazy('websites:list')

    def get_context_data(self, **kwargs):
        context = super(WebsiteDeleteView, self).get_context_data()
        context['linkActive'] = 'Websites'
        return context
