import json
from rest_framework.test import APITestCase
from .models import Author, Book


class BookTestsCreate(APITestCase):

    def test_create_book(self):
        book = Book.objects.create(name='Dune', edition= 1, publication_year= 2020)
        frank = Author.objects.create(name="Frank")
        book.authors.set([frank.pk])
        self.assertEqual(book.authors.count(), 1)

    def test_post_request_can_create_new_book(self):
        data = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 1965,
            "authors": [],
        }
        self.client.post(("/book/"), data=data)
        self.assertEqual(Book.objects.count(), 1)

    def test_delete_request_can_delete_book(self):
        data = {
            "name": "Dune",
            "edition": 1,
            "publication_year": 1965,
            "authors": [],
        }
        self.client.post(("/book/"), data=data)
        self.client.delete("/book/1/")
        self.assertEqual(Book.objects.count(), 0)

    def test_put_request_can_update_book(self):
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
        self.client.post(("/book/"), data=data)
        self.client.put(("/book/1/"), data=data2)
        self.assertEqual(Book.objects.get(id=1).name, "Dune")

    def test_get_request_can_search_authors(self):
        author1 = {
            "name": "Frank Herbert",
            }
        author2 = {
            "name": "Isaac Asimov",
            }
        author3 = {
            "name": "Douglas Addams",
        }
        self.client.post(("/author/"), data=author1)
        self.client.post(("/author/"), data=author2)
        self.client.post(("/author/"), data=author3)
        response = (self.client.get("/author/?search=Frank"))
        teste = json.loads(response.content)
        self.assertEqual(teste["count"], 1)

    def test_get_request_can_retrieve_authors_data(self):
        author1 = {
            "name": "Frank Herbert",
            }
        author2 = {
            "name": "Isaac Asimov",
            }
        author3 = {
            "name": "Douglas Addams",
        }
        self.client.post(("/author/"), data=author1)
        self.client.post(("/author/"), data=author2)
        self.client.post(("/author/"), data=author3)
        response = self.client.get("/author/1/")
        teste = json.loads(response.content)
        self.assertEqual(teste["name"], "Frank Herbert")

    def test_get_request_can_filter_books(self):
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
        self.client.post(("/book/"), data=data)
        self.client.post(("/book/"), data=data2)
        response = (self.client.get("/book/?name=Dune"))
        teste = json.loads(response.content)
        self.assertEqual(teste["count"], 1)
