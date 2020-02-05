"""
Deletes all the records from database.
"""


def clean_db():
    # just for running from cmd
    import os
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'manager.settings')
    django.setup()

    # main code
    from customers.models import Customer
    from websites.models import Website

    for customer in Customer.objects.all():
        customer.delete()

    for website in Website.objects.all():
        website.delete()


if __name__ == '__main__':
    clean_db()
