from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from .serializers import BookSearchSerializer, BookListSerializer, AuthorSerializer, BookCreateSerializer
from .models import Book, Author
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework.backends import DjangoFilterBackend
from .filters import BookFilter


class BookViewset(ModelViewSet):
    """
    A simple ViewSet for CRUD operations with Books.
    """
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        """
            Method for registering Books 
        """
        serializer = BookCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            book = serializer.save()
            data['response'] = "Book registered with success"
        else:
            data = serializer.errors
        return Response(data) 

    def list(self, request):
        queryset = Book.objects.all()
        serializer = BookListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.get(id=pk)
        book = get_object_or_404(Book, pk=pk)
        serializer = BookListSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        event = Book.objects.get(id=pk)
        serializer = BookListSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        event = Book.objects.get(id=pk)
        serializer = BookListSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        book = Book.objects.get(id=pk)
        book.delete()
        return Response("Book removed")

class AuthorAPIView(RetrieveAPIView):
    """
    A View for Authors data.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get(self, request, pk=None):
        queryset = Author.objects.get(id=pk)
        author = AuthorSerializer(queryset)
        return Response(author.data)


class AuthorSearchView(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['name']


class Search(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSearchSerializer
    filter_class = BookFilter
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'edition', 'publication_year', 'authors']
