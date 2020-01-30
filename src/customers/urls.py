from django.urls import path

from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerListView

urlpatterns = [
    path('new/', CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
    path('all/', CustomerListView.as_view(), name='list'),
]
