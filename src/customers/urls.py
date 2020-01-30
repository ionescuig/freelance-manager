from django.urls import path

from .views import CreateCustomerView

urlpatterns = [
    path('new/', CreateCustomerView.as_view(), name='create'),
]
