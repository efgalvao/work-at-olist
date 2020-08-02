from rest_framework import serializers

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta(object):
        model = Author
        fields = ('id', 'name', 'books')


class BookSerializer(serializers.ModelSerializer):
    edition = serializers.IntegerField()
    publication_year = serializers.IntegerField()

    class Meta(object):
        model = Book
        fields = ['id', 'name', 'edition', 'publication_year', 'authors']
