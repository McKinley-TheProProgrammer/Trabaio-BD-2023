from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from datetime import date, datetime
import os, psycopg2, csv
from .auth import get_db_connection 
from .sqlRawExecute import *
import json

views = Blueprint('views',__name__)

# CREATE VIEW home ()
@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        descricao = request.form.get('note')
        nota = request.form.get('aval')
        if(len(descricao) < 1):
            flash('Avaliação muito pequena!!', category='error')
        elif(len(nota) < 1):
            flash('De uma Nota',category='error')
        else:
            connect = get_db_connection()
            #cursor.execute("SELECT * FROM Usuario")
            #note_list = cursor.fetchall()
            #print(len(note_list))
            #new_note = Note(note_list[0],new_note[1],new_note[2],note,nota,datetime.now()) #Schema

            with connect.cursor() as cursor:
                cursor.execute(SELECT_USER_FROM_ID)
                user = cursor.fetchone()[0]
                print(user)
                cursor.execute("INSERT INTO Nota(usuario_id,nota_disciplina,descricao,dataDePostagem) VALUES (%s,%s,%s,%s)", (user,int(nota),descricao,datetime.now()))
                cursor.execute(SELECT_NOTES)
                notes = cursor.fetchall()
                connect.commit()
                print(notes)

            #db.session.add(new_note)
            #db.session.commit()
            flash('Avaliação Enviada', category='success')

    return render_template("home.html",user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    #note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            #db.session.delete(note)
            #db.session.commit()
            return jsonify({})