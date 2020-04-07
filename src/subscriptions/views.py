from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import SubscriptionForm, SubscriptionUpdateForm
from .models import Subscription


def date_in_one_month():
    return date.today()+timedelta(days=31)


class SubscriptionCreateView(LoginRequiredMixin, CreateView):
    template_name = 'subscriptions/create.html'
    form_class = SubscriptionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(SubscriptionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SubscriptionCreateView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        return context


class SubscriptionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'subscriptions/detail.html'
    model = Subscription

    def get_context_data(self, **kwargs):
        context = super(SubscriptionDetailView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        return context


class SubscriptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'subscriptions/update.html'
    form_class = SubscriptionUpdateForm
    queryset = Subscription.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SubscriptionUpdateView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        return context


class SubscriptionListView(LoginRequiredMixin, ListView):
    template_name = 'subscriptions/list.html'
    model = Subscription

    def get_context_data(self, **kwargs):
        context = super(SubscriptionListView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        context['date_in_one_month'] = date_in_one_month()
        context['today'] = date.today()
        return context


class ProjectSubscriptionsListView(LoginRequiredMixin, ListView):
    """
    Subscriptions for a specific project.
    """
    template_name = 'subscriptions/list.html'
    model = Subscription

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Subscription.objects.filter(project_id=pk)

    def get_context_data(self, **kwargs):
        context = super(ProjectSubscriptionsListView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        return context


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'subscriptions/delete.html'
    model = Subscription
    success_url = reverse_lazy('subscriptions:list')

    def get_context_data(self, **kwargs):
        context = super(SubscriptionDeleteView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        return context


class SubscriptionExpireView(LoginRequiredMixin, ListView):
    template_name = 'subscriptions/list.html'
    model = Subscription
    queryset = Subscription.objects.filter(date_renewal__lte=date_in_one_month()).order_by('date_renewal')

    def get_context_data(self, **kwargs):
        context = super(SubscriptionExpireView, self).get_context_data()
        context['linkActive'] = 'Subscriptions'
        context['date_in_one_month'] = date_in_one_month()
        context['today'] = date.today()
        return context
