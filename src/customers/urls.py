from django.urls import path

from .views import CustomerCreateView, CustomerDetailView, CustomerListView

urlpatterns = [
    path('new/', CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('all/', CustomerListView.as_view(), name='list'),
]
