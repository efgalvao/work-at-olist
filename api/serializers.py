from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Book
        fields = '__all__'