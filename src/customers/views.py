from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'customers/create.html'
    form_class = CustomerForm
    # success_url = reverse_lazy('home')


class CustomerDetailView(LoginRequiredMixin, DetailView):
    template_name = 'customers/detail.html'
    model = Customer
