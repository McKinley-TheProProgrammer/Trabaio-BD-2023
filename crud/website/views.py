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
    disciplinas = get_courses()
    id = request.form.get('id')
    user = get_usuario(id)
    turma_id = get_turma(id)

    if request.method == 'POST':
        
        descricao = request.form.get('note')
        nota = request.form.get('aval')
       
        if(len(descricao) < 1):
            flash('Avaliação muito pequena!!', category='error')
        elif(len(nota) < 1):
            flash('De uma Nota',category='error')
        else:
            connect = get_db_connection()
            cursor = connect.cursor()

            
           
            cursor.execute("INSERT INTO Nota(nota_disciplina,descricao,dataDePostagem,usuario_id,turma_id) VALUES (%s,%s,%s,%s,%s)", (nota,descricao,datetime.now(),user,turma_id))
            cursor.execute(SELECT_NOTES)
            notes = cursor.fetchall()

            print("Notas: ",notes)

            connect.commit()
            

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
    #id = request.form['id']
    cursor.execute(SELECT_USERS)
    user = cursor.fetchone()
    conn.commit()

    return render_template("profile.html",usuario=user)