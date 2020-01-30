from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CustomerForm
from .models import Customer


class CreateCustomerView(LoginRequiredMixin, CreateView):
    template_name = "customers/create.html"
    form_class = CustomerForm
    success_url = reverse_lazy('home')
