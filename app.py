from flask import Flask, render_template, request, url_for, flash, redirect
import os
import sqlite3
import locale
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import abort
from datetime import date, datetime
from time import strptime

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
    # inclusao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    empresaid = db.Column(db.Integer, nullable=False)
    pessoa = db.Column(db.String(60), nullable=False)    
    data_inicio_ferias = db.Column(db.Date)
    data_fim_ferias = db.Column(db.Date)

    # data_inicio_ferias = db.Column(db.Date)
    # data_fim_ferias = db.Column(db.Date)
        
    # data_inicio_ferias = db.Column(strftime("%m/%d/%Y"))
    # data_fim_ferias = db.Column(strftime("%m/%d/%Y"))

    # data_inicio_ferias = db.DateTime(db.DateTime)
    # data_fim_ferias = db.DateTime(db.DateTime)
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

@app.route('/novo', methods=('GET', 'POST'))
def novo():
    if request.method == 'POST':
        empresaid = request.form.get('empresaid')
        pessoa = request.form.get('pessoa')

        data_inicio_ferias = datetime.strptime('data_inicio_ferias', '%Y-%m-%d').date()
        data_fim_ferias = datetime.strptime('data_fim_ferias', '%Y-%m-%d').date()


        # data_inicio_ferias = datetime.strptime('data_inicio_ferias', '%Y-%m-%d %H:%M:%S').date()
        # data_fim_ferias = datetime.strptime('data_fim_ferias', '%Y-%m-%d %H:%M:%S').date()

        # data_inicio_ferias = datetime.strptime('data_inicio_ferias', '%Y-%m-%d %H:%M:%S').date()
        # data_fim_ferias = datetime.strptime('data_fim_ferias', '%Y-%m-%d %H:%M:%S').date()

        # data_inicio_ferias = datetime.strptime('data_inicio_ferias', '%Y-%m-%d').date()
        # data_fim_ferias = datetime.strptime('data_fim_ferias', '%Y-%m-%d').date()

        #data_inicio_ferias = request.form['data_inicio_ferias']
        #data_fim_ferias = request.form['data_fim_ferias']
        
        # data_inicio_ferias=request.form.get('data_inicio_ferias')
        # data_fim_ferias=request.form.get('data_fim_ferias')
        # data_inicio_ferias=request.form.get('db.DateTime')
        # data_fim_ferias=request.form.get('db.DateTime')        
        valor_ferias=request.form.get('valor_ferias').replace(',', '.')

        if not pessoa:
            flash('Campo obrigatório')
        else:
            novo = Controle_ferias(empresaid=empresaid, pessoa=pessoa, data_inicio_ferias=data_inicio_ferias, data_fim_ferias=data_fim_ferias, valor_ferias=valor_ferias)
            db.session.add(novo)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('novo.html')

@app.route('/<int:cf2_id>/editar', methods=('GET', 'POST'))
def editar(cf2_id):
    cf2 = get_post(cf2_id)

    if request.method == 'POST':
        empresaid = request.form['empresaid']
        pessoa = request.form['pessoa']
        # data_inicio_ferias = request.form['data_inicio_ferias']
        data_inicio_ferias = request.form['data_inicio_ferias']
        data_fim_ferias = request.form['data_fim_ferias']                
        valor_ferias = request.form['valor_ferias'].replace(',', '.')

        if not pessoa:
            flash('Campo obrigatório')
        else:
            cf2.empresaid = empresaid
            cf2.pessoa = pessoa
            # cf2.data_inicio_ferias = data_inicio_ferias
            data_inicio_ferias=request.form.get('db.Date')
            data_fim_ferias=request.form.get('db.Date')
            cf2.valor_ferias = valor_ferias
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('editar.html', cf2=cf2)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    cf2 = get_post(id)
    db.session.delete(cf2)
    db.session.commit()
    flash('"{}" foi apagado com sucesso!'.format(cf2.pessoa))
    return redirect(url_for('index'))
