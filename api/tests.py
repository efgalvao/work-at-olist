import csv
import json
import os

from django.core.management import call_command
from rest_framework.test import APITestCase

from .models import Author, Book


class BookTestsCreate(APITestCase):

    def test_import_authors_command(self):
        """
            Creates a .csv file, import a file, checks if is successful.
        """
        authors = [["name"], ["Frank Herbert"], ["Isaac Asimov"], ["Douglas Addams"],
                   ["Stephen King"], ["Philip K. Dick"], ["James S.A. Corey"]]
        filename = 'test_authors.csv'
        with open('test_authors.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(authors)
        call_command('import_authors', filename, '--test')
        os.remove(filename)
        authors = Author.objects.all()
        self.assertEqual(Author.objects.count(), len(authors))

    def test_create_author(self):
        """
            Creates an author object.
        """
        author = Author.objects.create(name='AAA')
        self.assertEqual(Author.objects.count(), 1)

    def test_post_request_can_create_new_author(self):
        """
            Creates an author object by post request.
        """
        data = {
            "name": "Robert Heilein",
        }
        self.client.post("/author/", data=data)
        self.assertEqual(Author.objects.count(), 1)

    def test_create_book(self):
        """
            Creates a book object.
        """
        book = Book.objects.create(name='Dune', edition=1, publication_year=2020)
        frank = Author.objects.create(name="Frank")
        book.authors.set([frank.pk])
        self.assertEqual(Book.objects.count(), 1)

    def test_post_request_can_create_new_book(self):
        """
            Creates a book object by post request.
        """
        data = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 1965,
            "authors": [],
        }
        self.client.post("/book/", data=data)
        self.assertEqual(Book.objects.count(), 1)

    def test_get_request_can_retrieve_authors_data(self):
        """
            Retrieves authors data.
        """
        data = {
            "name": "Frank Herbert",
        }
        self.client.post("/author/", data=data)
        response = self.client.get("/author/1/")
        test = json.loads(response.content)
        # print(test)
        self.assertEqual(test["name"], "Frank Herbert")

    def test_get_request_can_retrieve_book_data(self):
        """
            Retrieves books data.
        """
        data = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 1965,
            "authors": [],
        }
        self.client.post("/book/", data=data)
        response = self.client.get("/book/1/")
        test = json.loads(response.content)
        self.assertEqual(test["name"], "Dune")

    def test_put_request_can_update_book(self):
        """
            Updates a book with a update request.
        """
        data = {
            "name": "Foundation",
            "edition": 1,
            "publication_year": 1942,
            "authors": [],
        }
        data2 = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 1965,
            "authors": [],
        }
        self.client.post("/book/", data=data)
        self.client.put("/book/1/", data=data2)
        self.assertEqual((Book.objects.get(id=1)).name, "Dune")

    def test_patch_request_can_update_book(self):
        """
            Updates a book with a patch request.
        """
        data = {
            "name": "Found",
            "edition": 1,
            "publication_year": 1942,
            "authors": [],
        }
        data2 = {
            "name": "Foundation",
        }
        self.client.post("/book/", data=data)
        self.client.patch("/book/1/", data=data2)
        self.assertEqual((Book.objects.get(id=1)).name, "Foundation")

    def test_delete_request_can_delete_book(self):
        """
            Deletes a book with a delete request.
        """
        data = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 1965,
            "authors": [],
        }
        self.client.post("/book/", data=data)
        self.client.delete("/book/1/")
        self.assertEqual(Book.objects.count(), 0)

    def test_get_request_can_filter_books(self):
        """
            Filter books.
        """
        data = {
            "name": "Foundation",
            "edition": 1,
            "publication_year": 1942,
            "authors": [],
        }
        data2 = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 2020,
            "authors": [],
        }
        self.client.post("/book/", data=data)
        self.client.post("/book/", data=data2)
        response = (self.client.get("/book/?name=Dune"))
        teste = json.loads(response.content)
        self.assertEqual(teste["count"], 1)

    def test_get_request_can_search_authors(self):
        """
            Searches author by name.
        """
        author1 = {
            "name": "Frank Herbert",
        }
        author2 = {
            "name": "Isaac Asimov",
        }
        author3 = {
            "name": "Douglas Addams",
        }
        self.client.post("/author/", data=author1)
        self.client.post("/author/", data=author2)
        self.client.post("/author/", data=author3)
        response = (self.client.get("/author/?search=Frank"))
        test = json.loads(response.content)
        self.assertEqual(test["count"], 1)
