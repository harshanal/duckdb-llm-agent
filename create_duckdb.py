import duckdb

con = duckdb.connect('ducks.duckdb')
con.execute('''
    CREATE TABLE ducks (
        id INTEGER,
        species TEXT,
        age INTEGER
    )
''')
con.execute("INSERT INTO ducks VALUES (1, 'Mallard', 3), (2, 'Teal', 2), (3, 'Pekin', 5)")
con.close()
