from django.urls import path

from .views import SubscriptionCreateView, SubscriptionDeleteView, SubscriptionDetailView, SubscriptionListView,\
    SubscriptionUpdateView, SubscriptionExpireView

urlpatterns = [
    path('new/', SubscriptionCreateView.as_view(), name='create'),
    path('<int:pk>/', SubscriptionDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', SubscriptionDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', SubscriptionUpdateView.as_view(), name='update'),
    path('', SubscriptionListView.as_view(), name='list'),
    path('expire/', SubscriptionExpireView.as_view(), name='list_expire'),
]
