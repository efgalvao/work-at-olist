import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from sqlalchemy import create_engine


class Command(BaseCommand):
    help = 'Import Authors from a CSV file to DB'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

        # Named (optional) arguments for testing purpose
        parser.add_argument(
            '--test',
            action='store_true',
            help='Test command with a Sqlite3 DB',
        )

    def handle(self, *args, **options):

        try:
            file = options['file']
        except FileNotFoundError:
            raise CommandError("File not found")
        except TypeError:
            raise CommandError("A CSV type file is required")

        if options['test']:
            engine = create_engine('sqlite:///db.sqlite3')
            connection = engine.connect()

        else:
            engine = create_engine('postgresql+psycopg2://myuser:mypass@localhost/mydb')
            connection = engine.connect()

        try:
            for df in pd.read_csv(file, chunksize=1000):
                df.to_sql(
                    'api_author',
                    connection,
                    index=False,
                    if_exists='append'  # if the table already exists, append data
                )
            connection.close()
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {file}"))
        except Exception:
            raise CommandError(f"There was an error while importing {file}")
