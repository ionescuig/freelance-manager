from django.urls import path

from .views import WebsiteCreateView, WebsiteDeleteView, WebsiteListView, WebsiteUpdateView

urlpatterns = [
    path('new/', WebsiteCreateView.as_view(), name='create'),
    path('<int:pk>/delete', WebsiteDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', WebsiteUpdateView.as_view(), name='update'),
    path('', WebsiteListView.as_view(), name='list'),
]
