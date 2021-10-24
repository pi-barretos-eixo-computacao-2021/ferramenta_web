from flask import Flask, render_template
import os, datetime, time
import sqlite3
import locale
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))

app = Flask('__name__')
app.config['SECRET_KEY'] = 'Senha*659'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

def format_currency(value):
    return "R${:,.2f}".format(value)

class Controle_ferias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inclusao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    empresaid = db.Column(db.Integer, nullable=False)
    pessoa = db.Column(db.String(60), nullable=False)
    data_inicio_ferias = db.Column(db.Date, nullable=False)
    data_fim_ferias = db.Column(db.Date, nullable=False)
    valor_ferias = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    cf = Controle_ferias.query.all()
    return render_template('index.html', cf=cf)

def get_post(cf2_id):
    cf2 = Controle_ferias.query.filter_by(id=cf2_id).first()
    if cf2 is None:
        abort(404)
    return cf2

@app.route('/<int:cf2_id>')
def cf2(cf2_id):
    cf2 = get_post(cf2_id)
    return render_template('controle_ferias.html', cf2=cf2)
    