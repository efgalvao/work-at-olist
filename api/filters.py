from .models import Book
import django_filters

class BookFilter(django_filters.FilterSet):
    authors = django_filters.CharFilter(
        field_name='authors__name')
    class Meta:
        model = Book
        fields = ['name', 'edition', 'publication_year', 'authors']



