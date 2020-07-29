        try:
            file = kwargs['file']
        except FileNotFoundError:
            raise CommandError("File not found")
        except TypeError:
            raise CommandError("A CSV type file is required")

        try:
            dfs = pd.read_csv(file, index_col='name', chunksize=10000)
            engine = create_engine('sqlite:///db.sqlite3')
            sqlite_connection = engine.connect()
            sqlite_table = "api_author"
            for df in dfs:
                df.to_sql(sqlite_table, sqlite_connection, if_exists='append')
            sqlite_connection.close()
            self.stdout.write(self.style.SUCCESS(f"Successfully imported authors."))
        except Exception:
            raise CommandError("There was an error while importing the file")