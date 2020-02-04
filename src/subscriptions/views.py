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


class ProjectSubscriptionsListView(LoginRequiredMixin, ListView):
    """
    Subscriptions for a specific project.
    """
    template_name = 'subscriptions/list.html'
    model = Subscription

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Subscription.objects.filter(project_id=pk)


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'subscriptions/delete.html'
    model = Subscription
    success_url = reverse_lazy('subscriptions:list')


def date_renewal_default():
    from datetime import date, timedelta
    return date.today()+timedelta(days=31)


class SubscriptionExpireView(LoginRequiredMixin, ListView):
    template_name = 'subscriptions/list-expire.html'
    model = Subscription
    queryset = Subscription.objects.filter(date_renewal__lte=date_renewal_default()).order_by('date_renewal')
