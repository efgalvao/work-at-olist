from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django_filters.rest_framework.backends import DjangoFilterBackend
from .serializers import BookFilterSerializer, BookListSerializer
from .serializers import AuthorSerializer, BookCreateSerializer
from .models import Book, Author
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
        """
            Method for listing books  
        """
        queryset = Book.objects.all()
        serializer = BookListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
            Method for retrieving a specific book 
        """
        book = get_object_or_404(Book, pk=pk)
        serializer = BookListSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
            Method for updating a specific book 
        """
        event = Book.objects.get(id=pk)
        serializer = BookListSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """
            Method for a partial update of a specific book 
        """
        event = Book.objects.get(id=pk)
        serializer = BookListSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
            Method for removing a specific book 
        """
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
        """
            Method for retrieving a specific authors data 
        """
        author = get_object_or_404(Author, pk=pk)
        queryset = AuthorSerializer(author)
        return Response(queryset.data)


class AuthorSearchView(ListAPIView):
    """
        Endpoint for searching for a specific author 
    """
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['name']


class BookSearch(ListAPIView):
    """
        Endpoint for filtering books 
    """
    queryset = Book.objects.all()
    serializer_class = BookFilterSerializer
    filter_class = BookFilter
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name', 'edition', 'publication_year', 'authors']
