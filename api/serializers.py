from rest_framework import serializers
from .models import Author, Book

class BookCreateSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']

class BookListSerializer(serializers.ModelSerializer):
    #authors =  serializers.StringRelatedField(source='authors', many=True)

    class Meta(object):
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']

class BookSearchSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta(object):
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    
    class Meta(object):
        model = Author
        fields = ('id', 'name', 'books')




