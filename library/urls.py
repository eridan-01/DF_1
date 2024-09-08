from django.urls import path
from .views import AuthorListAPIView, AuthorCreateAPIView, AuthorRetrieveAPIView, AuthorUpdateAPIView, \
    AuthorDestroyAPIView, BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, \
    BookDestroyAPIView, BookIssueListAPIView, BookIssueCreateAPIView, BookIssueRetrieveAPIView, BookIssueUpdateAPIView, \
    BookIssueDestroyAPIView
from library.apps import LibraryConfig

app_name = LibraryConfig.name

urlpatterns = [
    # Authors
    path('authors/', AuthorListAPIView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateAPIView.as_view(), name='author-create'),
    path('authors/<int:pk>/', AuthorRetrieveAPIView.as_view(), name='author-retrieve'),
    path('authors/<int:pk>/update/', AuthorUpdateAPIView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', AuthorDestroyAPIView.as_view(), name='author-delete'),

    # Books
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookRetrieveAPIView.as_view(), name='book-retrieve'),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDestroyAPIView.as_view(), name='book-delete'),

    # Book issues
    path('issues/', BookIssueListAPIView.as_view(), name='issues-list'),
    path('issues/create/', BookIssueCreateAPIView.as_view(), name='issues-create'),
    path('issues/<int:pk>/', BookIssueRetrieveAPIView.as_view(), name='issues-retrieve'),
    path('issues/<int:pk>/update/', BookIssueUpdateAPIView.as_view(), name='issues-update'),
    path('issues/<int:pk>/delete/', BookIssueDestroyAPIView.as_view(), name='issues-delete'),
]