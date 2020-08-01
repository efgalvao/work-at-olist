from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer



class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class BookView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'edition', 'publication_year', 'authors')


    def create(self, request, *args, **kwargs):
        """
            Method for registering Books
        """
        serializer = BookSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Book registered with success"
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
