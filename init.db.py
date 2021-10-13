import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect('database.db')

''' with open ('schema.sql') as f:
    connection.executescript(f.read()) '''

cur = connection.cursor()

cur.execute("INSERT INTO controle_ferias(inclusao, empresaid, pessoa, data_inicio_ferias, data_fim_ferias, valor_ferias) VALUES (?, ?)",
            ('13/10/2021', '01', 'SÉRGIO CARLOS', '25/10/2021', '24/11/2021', '1670.50')
            )

cur = connection.cursor()

connection.commit()
connection.close()