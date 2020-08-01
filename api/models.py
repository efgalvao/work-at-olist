from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Book(models.Model):
    name = models.CharField("Name", max_length=100)
    edition = models.PositiveIntegerField("Edition", default=1)
    publication_year = models.PositiveIntegerField("Publication Year")
    authors = models.ManyToManyField(Author, related_name='books', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
