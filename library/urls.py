from django.urls import path
from .views import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView
from library.apps import LibraryConfig

app_name = LibraryConfig.name

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),
]