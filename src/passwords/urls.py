from django.urls import path

from .views import PasswordCreateView, PasswordDeleteView, PasswordDetailView, PasswordListView, PasswordUpdateView

urlpatterns = [
    path('new/', PasswordCreateView.as_view(), name='create'),
    path('<int:pk>/', PasswordDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', PasswordDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', PasswordUpdateView.as_view(), name='update'),
    path('', PasswordListView.as_view(), name='list'),
]
