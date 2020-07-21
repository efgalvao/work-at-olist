from django.core.management.base import BaseCommand, CommandError
import csv
from models import Author

class Command(BaseCommand):
    help = 'Import Authors from CSV to DB'
    

    def handle(self, *args, **kwargs):
        
                

        