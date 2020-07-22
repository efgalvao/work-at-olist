from django.core.management.base import BaseCommand, CommandError
import pandas as pd
from sqlalchemy import create_engine


class Command(BaseCommand):
    help = 'Import Authors from CSV to DB'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
    

    def handle(self, *args, **kwargs):
        file = kwargs['file']
        dfs = pd.read_csv(file, index_col='name', chunksize=10000)
        engine = create_engine('sqlite:///db.sqlite3')
        sqlite_connection = engine.connect()
        sqlite_table = "api_author"
        for df in dfs:
            df.to_sql(sqlite_table, sqlite_connection, if_exists='append')
        sqlite_connection.close()
