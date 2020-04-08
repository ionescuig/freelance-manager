from datetime import date, timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from .models import Subscription


"""
NOT WORKING YET

daily:
    check for subscriptions that will expire in exactly 1 month
    send mail ONLY if there are subscriptions that will expire in exactly 1 month
weekly (Monday):
    check for subscriptions expired and subscriptions that will expire in the month
    send mail ONLY if there are subscriptions in any of these categories
    
To Do:
    Set:
        Context
    Transform into functions
    
"""

"""to be deleted
for every function

to be set
  context:
      user: name, email
      subscriptions (about to expire)
      subscriptions_expired

      for daily email: subs that will expire in 1 month exactly
"""

# outside functions:
date_today = date.today()
date_in_one_month = date.today() + timedelta(days=30)

from_email = settings.DEFAULT_FROM_EMAIL
recipient_list = [settings.DEFAULT_TO_EMAIL]

users = User.objects.exclude(email__isnull=True).exclude(email__exact='')


def send_mail_with_subscriptions_that_will_expire_in_exactly_one_month():
    """ should run daily"""

    subscriptions_in_one_month_exactly = user.subscriptions.filter(
        notify_by_email=True).filter(
        date_renewal__iexact=date_in_one_month)
    pass


def send_mail_with_subscriptions_expired_and_about_to_expire():
    """ should run weekly"""

    subject = 'Freelance Manager: Subscriptions that will expire in the next month'
    message = 'testing'

    template_name = 'subscriptions/email_html_message_expired.html'
    for user in users:
        subscriptions_expired = user.subscriptions.filter(
            notify_by_email=True).filter(
            date_renewal__lte=date_today)
        subscriptions_in_one_month = user.subscriptions.filter(
            notify_by_email=True).filter(
            date_renewal__lte=date_in_one_month).filter(
            date_renewal__gt=date_today)

        context = {
            'name': user.username,
            'email': user.email,
            'subscriptions_expired': subscriptions_expired,
            'subscriptions_in_one_month': subscriptions_in_one_month,
        }
        html_content = render_to_string(template_name, context)

        send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,
                html_message=html_content
        )

        from celery.utils.log import get_task_logger
        logger = get_task_logger(__name__)
        logger.info(recipient_list)
