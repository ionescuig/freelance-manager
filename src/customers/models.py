from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    # main data
    name    = models.CharField(max_length=35)
    email   = models.EmailField()
    phone   = models.CharField(
        validators=[RegexValidator(regex='^0\d{10}$', message='Please use a valid phone number', code='nomatch')],
        max_length=11)

    # additional data
    town = models.CharField(max_length=20, default='Plymouth')
    country = models.CharField(max_length=20, default='Great Britain')
    company             = models.CharField(max_length=35, blank=True)
    address_first_line  = models.CharField(max_length=35, blank=True)
    post_code           = models.CharField(max_length=9, blank=True)

    # bank data
    sort_code       = models.CharField(
        validators=[RegexValidator(regex='^\d{6}$', message='Invalid sort code', code='nomatch')],
        max_length=6, blank=True)
    account_no      = models.CharField(
        validators=[RegexValidator(regex='^\d{8}$', message='Invalid account number. If the account number has less than 8 digits, please add 0(zero) in front.', code='nomatch')],
        max_length=8, blank=True)
    iban            = models.CharField(
        validators=[RegexValidator(regex='^[0-9A-Z]{15,32}$', message='Invalid IBAN. Please use CAPITAL LETTERS.', code='nomatch')],
        max_length=32, blank=True)
    card_no         = models.CharField(
        validators=[RegexValidator(regex='^\d{16}$', message='Invalid card number', code='nomatch')],
        max_length=16, blank=True)
    card_exp_date   = models.DateField(blank=True, null=True)

    # obs
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.company:
            return self.company + ' (' + self.name + ')'
        else:
            return self.name

    def clean(self):
        if self.card_exp_date:
            if self.card_exp_date < date.today():
                raise ValidationError({"card_exp_date": ValidationError("Card expired or wrong date")})

    def get_absolute_url(self):
        return reverse('customers:detail', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['company', 'name']
