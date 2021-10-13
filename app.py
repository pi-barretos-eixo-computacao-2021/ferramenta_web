from flask import Flask, render_template
import os, datetime
import sqlite3
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqLite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'Senha*659'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

''' class controle_ferias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inclusao = db.Column(db.Datetime, default=datetime.datetime.utcnow)
    empresaid = db.Column(db.Integer(3), nulltable=False)
    pessoa = db.Column(db.String(60), nulltable=False)
    data_inicio_ferias = db.Column(db.Date, nulltable=False)
    data_fim_ferias = db.Column(db.Date, nulltable=False)
    valor_ferias = db.Column(db.Decimal(6,2), nulltable=False) '''

@app.route('/')
def index():
    return render_template('index.html')

