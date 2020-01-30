from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import SubscriptionForm
from .models import Subscription


class SubscriptionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'subscriptions/create.html'
    form_class = SubscriptionForm


class SubscriptionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'subscriptions/detail.html'
    model = Subscription


class SubscriptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'subscriptions/update.html'
    form_class = SubscriptionForm
    queryset = Subscription.objects.all()


class SubscriptionListView(LoginRequiredMixin, ListView):
    template_name = 'subscriptions/list.html'
    model = Subscription


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'subscriptions/delete.html'
    model = Subscription
    success_url = reverse_lazy('subscriptions:list')
