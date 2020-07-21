from django.core.management.base import BaseCommand, CommandError
import csv
from api.models import Author

class Command(BaseCommand):
    help = 'Import Authors from CSV to DB'

    def add_arguments(self, parser):
        parser.add_argument('file', type=list, help='File for get names')

    def handle(self, *args, **kwargs):
        file = kwargs['file']
        with open(file "r") as authors:
            reader = csv.reader()
            next(reader, None) 
            for row in reader:
                print(row)
                authors= Author.objects.create(row)
            
        
       