from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    edition = models.CharField(max_length=10)
    publication_year = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.name
