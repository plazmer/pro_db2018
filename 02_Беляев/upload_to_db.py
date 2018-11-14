import sqlite3
import csv

db = sqlite3.connect('storage/02.db')
cursor = db.cursor()


def gen_iterator(filename):
    file = open(filename, 'r')
    reader = csv.DictReader(file, dialect='excel', delimiter=';')
    for row in reader:
        if row.get(None, False):
            row.pop(None)
        vals = row.values()
        yield tuple(vals)


def insert_into_db(iter):
    cursor.executemany("""INSERT INTO phones 
                          (`code`, `from`, `to`, `count`, `provider`, `region`)
                          VALUES
                           (?, ?, ?, ?, ?, ?)""", iter)
    db.commit()


def insert_from_files(files):
    for file in files:
        iterator = gen_iterator(file + '.csv')
        insert_into_db(iterator)


insert_from_files(['ABC-3x', 'ABC-4x', 'ABC-8x', 'DEF-9x'])
