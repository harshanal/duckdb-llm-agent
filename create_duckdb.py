import duckdb

con = duckdb.connect('ducks.duckdb')
con.execute("DROP TABLE IF EXISTS ducks;")
con.execute('''
    CREATE TABLE ducks (
        id VARCHAR,
        color VARCHAR,
        firstName VARCHAR,
        lastName VARCHAR,
        gender VARCHAR,
        age INTEGER
    )
''')
con.execute('''
    INSERT INTO ducks VALUES 
    ('kA0gKL', 'red', 'Marty', 'McFly', 'male', 25),
    ('dx3ngL', 'teal', 'Duckota', 'Duck', 'female', 30),
    ('FQd4uL', 'yellow', 'Fanning', 'Norris', 'male', 22),
    ('J9s7ZZ', 'red', 'James', 'Pond', 'male', 28),
    ('ZM5uJL', 'black', 'Darth', 'Wader', 'male', 35),
    ('o5FukA', 'yellow', 'Clint', 'Beakwood', 'male', 40),
    ('wKqP2D', 'yellow', 'Mary', 'Quackens', 'female', 27),
    ('CQAb5l', 'orange', 'Ducky', 'Balboa', 'male', 33),
    ('eKiYA5', 'orange', 'Captain', 'Quack', 'male', 29),
    ('YiS0Q1', 'teal', 'Wonder', 'Duck', 'female', 31)
''')

con.close()
