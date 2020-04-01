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
        today = date.today()
        in_one_month = date.today() + timedelta(days=30)
        context = super(HomePageView, self).get_context_data()
        customers = Customer.objects.all()
        projects = Project.objects.all()
        subscriptions_all = Subscription.objects.all()
        subscriptions_in_one_month = Subscription.objects.filter(
            date_renewal__lte=in_one_month).filter(date_renewal__gt=today)
        subscriptions_expired = Subscription.objects.filter(date_renewal__lte=today)
        passwords = Password.objects.all()
        websites = Website.objects.all()
        context.update({
            'linkActive': 'Home',
            'customers': customers,
            'projects': projects,
            'subscriptions': subscriptions_all,
            'subscriptions_in_one_month': subscriptions_in_one_month,
            'subscriptions_expired': subscriptions_expired,
            'passwords': passwords,
            'websites': websites,

        })
        return context
