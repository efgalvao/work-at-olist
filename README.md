## Project Description:

This project is built on Python and Django Rest Framework, it provides a REST API for a library to store book and authors data. 

This project was made following the instructions from the work at olist challenge:
https://github.com/olist/work-at-olist
 


## Instalation instructions:

To run this project it's necessary to have python >= 3.5 installed and follow the steps below:

* Clone the github repository:
```
    $ git clone https://github.com/efgalvao/work-at-olist
``` 

* Create a virtual environment:
```
$ python3 -m venv venv
```
* Activate it:
```
$ source ./venv/bin/activate
```
* Install the requirements:
```
$ pip install -r requirements.txt
```
* Create a .env file at the same folder of settings.py with the following entry:
```
SECRET_KEY=YourSecretKey
```
* Migrate the database:
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```
* Import Authors file(only after migrate):
```
$ python3 manage.py import_authors authors.csv
```
* Run the server:
```
$ python3 manage.py runserver
```
## Testing:
* To run tests:
```
$ python3 manage.py test
```

## This application is deployed on heroku: 
### https://library-api-olist.herokuapp.com/



# Endpoints:
### Author endpoint:
```
/author/
    get:
      List all authors
    post:
      Create an author
/author/?search={name}
    get:
      Search for an author
/author/{id}/:
    get:
      Retrieve an author by id
    put:
      Update an author
    patch:
      Partially update an author
    delete:
      Delete an author
```
### Book endpoint:
```
/book/
    get:
      List all books
    post:
      Create a book
/book/?name={name}
    get:
      Filter books according to name.(All filters can be used in any combination or all together.
/book/?edition={edition}
    get:
      Filter books according to edition.(All filters can be used in any combination or all together.
/book/?publication_year={publication_year}
    get:
      Filter books according to publication year.(All filters can be used in any combination or all together.
/book/?authors={id}
    get:
      Filter books according to authors id.(All filters can be used in any combination or all together.
/book/{id}/:
    get:
      Retrieve an book by id.
    put:
      Update a book
    patch:
      Partially update a book
    delete:
      Delete a book
```
## Usage Instructions:
* To create/update a book you need to send this payload (in json format) below:
```
{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors": // List of author ids, same ids of imported data
}
```
* To see the OpenAPI schema you can access:

https://library-api-olist.herokuapp.com/openapi

## Work environment:
* Inspiron Laptop:
  - Processor: Intel Core i3
  - Memory: 4GB RAM
  - Graphic card: Integrated
  - Storage: 500 GB
  - Operating System: Linux Mint
    
* IDE:
  - Pycharm Comunnity Edition
  
