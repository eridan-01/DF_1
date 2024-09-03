from rest_framework import generics
from .models import Author
from .serializers import AuthorSerializer


# Получение списка всех авторов и создание нового автора
class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Получение, обновление и удаление автора по ID
class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
