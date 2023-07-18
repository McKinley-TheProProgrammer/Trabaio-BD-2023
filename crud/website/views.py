from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import login_required, current_user

from datetime import date, datetime
import os, psycopg2, csv
from .auth import get_db_connection 
from .sqlRawExecute import *
import json

views = Blueprint('views',__name__)

# CREATE VIEW home ()
@views.route('/', methods=['GET','POST'])
def home():
    notes = []
    disciplinas = []
    if request.method == 'POST':
        id = request.form.get('id')
        descricao = request.form.get('note')
        nota = request.form.get('aval')
        user = get_usuario(id)
        turma_id = get_turma(id)
        if(len(descricao) < 1):
            flash('Avaliação muito pequena!!', category='error')
        elif(len(nota) < 1):
            flash('De uma Nota',category='error')
        else:
            connect = get_db_connection()
            cursor = connect.cursor()

           
            cursor.execute("INSERT INTO Nota(nota_disciplina,descricao,dataDePostagem,usuario_id,turma_id) VALUES (%s,%s,%s,%s,%s)", (nota,descricao,datetime.now(),id,id))
            cursor.execute(SELECT_NOTES)
            notes = cursor.fetchall()

            cursor.execute(SELECT_DISCIPLINAS)
            disciplinas = cursor.fetchall()

            connect.commit()
            print(notes)

            cursor.close()
            connect.close()
    
            flash('Avaliação Enviada', category='success')

    return render_template("home.html",note=notes,disciplines=disciplinas)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    #note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
          
            return jsonify({})
        
@views.route('/profile',methods=['GET','POST'])
def profile():

    conn = get_db_connection()

    cursor = conn.cursor()
    id = request.form['id']
    cursor.execute(SELECT_USERS)
    user = cursor.fetchone()
    conn.commit()

    return render_template("profile.html",us=user)