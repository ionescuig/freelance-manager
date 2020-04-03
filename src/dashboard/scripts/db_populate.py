"""
Populates the database.
"""


def populate_db():
    # just for running from cmd
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')
    django.setup()

    # main code
    from datetime import date, timedelta
    from customers.models import Customer
    from passwords.models import Password
    from projects.models import Project
    from subscriptions.models import Subscription
    from websites.models import Website

    from django.contrib.auth import get_user_model
    User = get_user_model()
    user = User.objects.filter(username__iexact='manager')[0]

    # ================
    # Create Customers
    # ================
    customer1 = Customer.objects.get_or_create(
        user=user,
        name='John Doe',
        email='john.doe@email.com',
        phone='01752123456',
        company='Paralex',
        town='Cardiff')
    customer2 = Customer.objects.get_or_create(
        user=user,
        name='Adam Smith',
        email='adam.smith@email.com',
        phone='01754234567')
    customer3 = Customer.objects.get_or_create(
        user=user,
        name='Ann Frazer',
        email='ann.frazer@email.com',
        phone='01723456789',
        company='Windology',
        town='London')
    customer4 = Customer.objects.get_or_create(
        user=user,
        name='Mark Whites',
        email='mark.whites@email.com',
        phone='01711258369')
    customer5 = Customer.objects.get_or_create(
        user=user,
        name='Kim Morgan',
        email='kim.morgan@email.com',
        phone='01722225588')

    # ===============
    # Create Projects
    # ===============
    project1 = Project.objects.get_or_create(
        user=user,
        customer=Customer.objects.get(name='John Doe'),
        name='Facebook')
    project2 = Project.objects.get_or_create(
        user=user,
        customer=Customer.objects.get(name='John Doe'),
        name='Instagram')
    project3 = Project.objects.get_or_create(
        user=user,
        customer=Customer.objects.get(name='Adam Smith'),
        name='Whatsapp')
    project4 = Project.objects.get_or_create(
        user=user,
        customer=Customer.objects.get(name='Ann Frazer'),
        name='Zoopla')
    project5 = Project.objects.get_or_create(
        user=user,
        customer=Customer.objects.get(name='Kim Morgan'),
        name='Digitax')

    # ===============
    # Create Websites
    # ===============
    website1 = Website.objects.get_or_create(
        user=user,
        name='Digital Ocean',
        url='https://www.digitalocean.com')
    website2 = Website.objects.get_or_create(
        user=user,
        name='GitHub',
        url='https://www.github.com')
    website3 = Website.objects.get_or_create(
        user=user,
        name='Heroku',
        url='https://www.heroku.com')

    # ====================
    # Create Subscriptions
    # ====================
    today = date.today()
    subscription1 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Facebook'),
        website=Website.objects.get(name='GitHub'),
        date_created=today - timedelta(days=365) + timedelta(days=15),
        date_renewal=today + timedelta(days=15))
    subscription2 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Facebook'),
        website=Website.objects.get(name='Heroku'),
        date_created=today - timedelta(days=365) + timedelta(days=80),
        date_renewal=today + timedelta(days=80))
    subscription3 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Instagram'),
        website=Website.objects.get(name='GitHub'),
        date_created=today - timedelta(days=365) + timedelta(days=-43),
        date_renewal=today + timedelta(days=-43))
    subscription4 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Instagram'),
        website=Website.objects.get(name='Heroku'),
        date_created=today - timedelta(days=365) + timedelta(days=52),
        date_renewal=today + timedelta(days=52))
    subscription5 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Whatsapp'),
        website=Website.objects.get(name='Digital Ocean'),
        date_created=today - timedelta(days=365) + timedelta(days=-22),
        date_renewal=today + timedelta(days=-22))
    subscription6 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Zoopla'),
        website=Website.objects.get(name='GitHub'),
        date_created=today - timedelta(days=365) + timedelta(days=72),
        date_renewal=today + timedelta(days=72))
    subscription7 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Whatsapp'),
        website=Website.objects.get(name='Heroku'),
        date_created=today - timedelta(days=365) + timedelta(days=57),
        date_renewal=today + timedelta(days=57))
    subscription8 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Zoopla'),
        website=Website.objects.get(name='GitHub'),
        date_created=today - timedelta(days=365) + timedelta(days=22),
        date_renewal=today + timedelta(days=22))
    subscription8 = Subscription.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Whatsapp'),
        website=Website.objects.get(name='GitHub'),
        date_created=today - timedelta(days=365) + timedelta(days=11),
        date_renewal=today + timedelta(days=11))

    # ================
    # Create Passwords
    # ================
    password1 = Password.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Facebook'),
        website=Website.objects.get(name='GitHub'),
        username='user',
        password='password')
    password2 = Password.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Facebook'),
        website=Website.objects.get(name='Heroku'),
        username='user',
        password='password')
    password3 = Password.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Instagram'),
        website=Website.objects.get(name='GitHub'),
        username='user',
        password='password')
    password4 = Password.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Instagram'),
        website=Website.objects.get(name='Heroku'),
        username='user',
        password='password')
    password5 = Password.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Whatsapp'),
        website=Website.objects.get(name='GitHub'),
        username='user',
        password='password')
    password6 = Password.objects.get_or_create(
        user=user,
        project=Project.objects.get(name='Whatsapp'),
        website=Website.objects.get(name='Heroku'),
        username='user',
        password='password')


if __name__ == '__main__':
    populate_db()
