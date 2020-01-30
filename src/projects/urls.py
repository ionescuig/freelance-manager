from django.urls import path

from .views import ProjectCreateView, ProjectDeleteView, ProjectDetailView, ProjectListView, ProjectUpdateView

urlpatterns = [
    path('new/', ProjectCreateView.as_view(), name='create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', ProjectDeleteView.as_view(), name='delete'),
    path('<int:pk>/update', ProjectUpdateView.as_view(), name='update'),
    path('all/', ProjectListView.as_view(), name='list'),
]
