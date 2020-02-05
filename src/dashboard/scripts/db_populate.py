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
    from customers.models import Customer
    from passwords.models import Password
    from projects.models import Project
    from subscriptions.models import Subscription
    from websites.models import Website

    customer1 = Customer.objects.get_or_create(name='John Doe', email='john.doe@email.com', phone='01752123456', company='Paralex', town='Cardiff')
    customer2 = Customer.objects.get_or_create(name='Adam Smith', email='adam.smith@email.com', phone='01754234567')
    customer3 = Customer.objects.get_or_create(name='Ann Frazer', email='ann.frazer@email.com', phone='01723456789', company='Windology', town='London')
    customer4 = Customer.objects.get_or_create(name='Mark Whites', email='mark.whites@email.com', phone='01711258369')
    customer5 = Customer.objects.get_or_create(name='Kim Morgan', email='kim.morgan@email.com', phone='01722225588')

    project1 = Project.objects.get_or_create(customer=Customer.objects.get(name='John Doe'), name='Facebook')
    project2 = Project.objects.get_or_create(customer=Customer.objects.get(name='John Doe'), name='Instagram')
    project3 = Project.objects.get_or_create(customer=Customer.objects.get(name='Adam Smith'), name='Whatsapp')
    project4 = Project.objects.get_or_create(customer=Customer.objects.get(name='Ann Frazer'), name='Zoopla')
    project5 = Project.objects.get_or_create(customer=Customer.objects.get(name='Kim Morgan'), name='Digitax')

    website1 = Website.objects.get_or_create(name='Digital Ocean', url='https://www.digitalocean.com')
    website2 = Website.objects.get_or_create(name='GitHub', url='https://www.github.com')
    website3 = Website.objects.get_or_create(name='Heroku', url='https://www.heroku.com')

    subscription1 = Subscription.objects.get_or_create(project=Project.objects.get(name='Facebook'), website=Website.objects.get(name='GitHub'), date_created='2020-01-10', date_renewal='2021-01-10')
    subscription2 = Subscription.objects.get_or_create(project=Project.objects.get(name='Facebook'), website=Website.objects.get(name='Heroku'), date_created='2020-01-15', date_renewal='2021-01-15')
    subscription3 = Subscription.objects.get_or_create(project=Project.objects.get(name='Instagram'), website=Website.objects.get(name='GitHub'), date_created='2019-02-10', date_renewal='2020-02-10')
    subscription4 = Subscription.objects.get_or_create(project=Project.objects.get(name='Instagram'), website=Website.objects.get(name='Heroku'), date_created='2019-02-15', date_renewal='2020-02-15')
    subscription5 = Subscription.objects.get_or_create(project=Project.objects.get(name='Whatsapp'), website=Website.objects.get(name='GitHub'), date_created='2019-02-20', date_renewal='2020-02-20')
    subscription6 = Subscription.objects.get_or_create(project=Project.objects.get(name='Whatsapp'), website=Website.objects.get(name='Heroku'), date_created='2020-01-10', date_renewal='2021-01-10')
    subscription7 = Subscription.objects.get_or_create(project=Project.objects.get(name='Zoopla'), website=Website.objects.get(name='GitHub'), date_created='2019-02-22', date_renewal='2020-02-22')

    password1 = Password.objects.get_or_create(project=Project.objects.get(name='Facebook'), website=Website.objects.get(name='GitHub'), username='user', password='password')
    password2 = Password.objects.get_or_create(project=Project.objects.get(name='Facebook'), website=Website.objects.get(name='Heroku'), username='user', password='password')
    password3 = Password.objects.get_or_create(project=Project.objects.get(name='Instagram'), website=Website.objects.get(name='GitHub'), username='user', password='password')
    password4 = Password.objects.get_or_create(project=Project.objects.get(name='Instagram'), website=Website.objects.get(name='Heroku'), username='user', password='password')
    password5 = Password.objects.get_or_create(project=Project.objects.get(name='Whatsapp'), website=Website.objects.get(name='GitHub'), username='user', password='password')
    password6 = Password.objects.get_or_create(project=Project.objects.get(name='Whatsapp'), website=Website.objects.get(name='Heroku'), username='user', password='password')


if __name__ == '__main__':
    populate_db()
