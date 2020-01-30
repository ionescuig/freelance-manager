from django.urls import path

from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerListView, CustomerUpdateView

urlpatterns = [
    path('new/', CustomerCreateView.as_view(), name='create'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', CustomerUpdateView.as_view(), name='update'),
    path('all/', CustomerListView.as_view(), name='list'),
]
