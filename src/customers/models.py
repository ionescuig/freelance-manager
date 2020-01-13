from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    name    = models.CharField(max_length=35)
    email   = models.EmailField()
    phone   = models.CharField(
        validators=[RegexValidator(regex='^0\d{10}$', message='Please use a valid phone number', code='nomatch')],
        max_length=11)                                      # maybe regex='^0[0-9]{10}$'

    company             = models.CharField(max_length=35)
    address_first_line  = models.CharField(max_length=35)
    town                = models.CharField(max_length=20, default='Plymouth')
    post_code           = models.CharField(max_length=9)
    country             = models.CharField(max_length=20, default='Great Britain')

    sort_code       = models.IntegerField(max_length=6)
    account_no      = models.IntegerField(max_length=8)
    iban            = models.CharField(max_length=34)       # add regex
    card_no         = models.IntegerField(max_length=16)    # add regex
    card_exp_date   = models.DateField()                    # add min=today

    obs = models.TextField()
