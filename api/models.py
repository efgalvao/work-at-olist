from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    edition = models.CharField(max_length=10, null=False, blank=False)
    publication_year = models.IntegerField(null=False, blank=False)
    authors = models.ManyToManyField(Author, related_name='books', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
