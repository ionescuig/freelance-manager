from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer
from projects.models import Project


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'customers/create.html'
    form_class = CustomerForm


class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customers/detail.html'
    model = Customer


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'customers/update.html'
    form_class = CustomerForm
    queryset = Customer.objects.all()


class CustomerListView(LoginRequiredMixin, ListView):
    template_name = 'customers/list.html'
    model = Customer


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'customers/delete.html'
    model = Customer
    success_url = reverse_lazy('customers:list')
