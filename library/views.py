from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.permissions import IsModer
from .models import Author, Book, BookIssue
from .paginators import CustomPagination
from .serializers import AuthorSerializer, BookSerializer, BookIssueSerializer
from rest_framework import serializers


class AuthorCreateAPIView(CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = (IsModer,)


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsModer,)


class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsModer,)


class AuthorDestroyAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsModer,)


class BookCreateAPIView(CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsModer,)


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "author__first_name", "author__last_name", "genre"]
    ordering_fields = ["published_date", "title"]
    ordering = ["title"]  # Сортировка по умолчанию


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsModer,)


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsModer,)


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsModer,)


class BookIssueCreateAPIView(CreateAPIView):
    serializer_class = BookIssueSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        if book.available_copies <= 0:
            raise serializers.ValidationError("Эта книга сейчас недоступна для выдачи.")

        # Уменьшение количества доступных копий книги
        book.available_copies -= 1
        book.save()
        serializer.save()


class BookIssueListAPIView(ListAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsModer,)
    pagination_class = CustomPagination


class BookIssueRetrieveAPIView(RetrieveAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsModer,)


class BookIssueUpdateAPIView(UpdateAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsModer,)

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.return_date:
            # Возвращаем книгу и увеличиваем количество доступных копий
            instance.book.available_copies += 1
            instance.book.save()


class BookIssueDestroyAPIView(DestroyAPIView):
    queryset = BookIssue.objects.all()
    serializer_class = BookIssueSerializer
    permission_classes = (IsModer,)
