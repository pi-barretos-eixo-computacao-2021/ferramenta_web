import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect('database.db')

with open ('schame.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()