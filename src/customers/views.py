from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer
from projects.models import Project


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'customers/create-update.html'
    form_class = CustomerForm

    def get_context_data(self, **kwargs):
        context = super(CustomerCreateView, self).get_context_data()
        context['linkActive'] = 'Customers'
        return context


class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customers/detail.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data()
        context['linkActive'] = 'Customers'
        return context


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'customers/create-update.html'
    form_class = CustomerForm
    queryset = Customer.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data()
        context['linkActive'] = 'Customers'
        return context


class CustomerListView(LoginRequiredMixin, ListView):
    template_name = 'customers/list.html'
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data()
        context['linkActive'] = 'Customers'
        return context


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'customers/delete.html'
    model = Customer
    success_url = reverse_lazy('customers:list')

    def get_context_data(self, **kwargs):
        context = super(CustomerDeleteView, self).get_context_data()
        context['linkActive'] = 'Customers'
        return context
