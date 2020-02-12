# Freelance Accounts Manager
##### Helps freelancers with keeping track of customers, projects, subscriptions and passwords
[Heroku](https://freelancemanager.herokuapp.com)
<br><br>
_work in progress_
___

Apps:
- customers
    - validation: existing customer, phone, sort code, account number, card number, IBAN, card expiry date.
- projects
    - contains all the subscriptions and passwords used when creating a new website for customers
- passwords
- subscriptions
    - validation: renewal date
- websites
    - used for subscriptions and passwords

<hr>

Next:
- for testing website: refresh database at least twice a day (celery tasks)
- send email when a subscription is about to expire (1 month, 1 week, 1 day)
- frontend
