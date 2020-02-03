from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from itertools import chain

from customers.models import Customer
from projects.models import Project
from subscriptions.models import Subscription
from passwords.models import Password
from websites.models import Website


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'home.html'

    def get_queryset(self):
        warning = date.today() + timedelta(days=30)
        return Subscription.objects.filter(date_renewal__lte=warning)

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data()
        customers = Customer.objects.all()
        projects = Project.objects.all()
        subscriptions = Subscription.objects.all()
        passwords = Password.objects.all()
        websites = Website.objects.all()
        context['customers'] = customers
        context['projects'] = projects
        context['subscriptions'] = subscriptions
        context['passwords'] = passwords
        context['websites'] = websites
        return context
