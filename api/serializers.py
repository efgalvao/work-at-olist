from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    
    class Meta(object):
        model = Author
        fields = ('name', 'books')

