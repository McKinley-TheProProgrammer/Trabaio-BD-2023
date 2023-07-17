from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, User
from datetime import date, datetime
import os, psycopg2, csv
from .auth import get_db_connection 
import json

views = Blueprint('views',__name__)

connect = get_db_connection()
cursor = connect.cursor()
# CREATE VIEW home ()
@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        nota = request.form.get('aval')
        if(len(note) < 1):
            flash('Avaliação muito pequena!!', category='error')
        else:
            
            #cursor.execute("SELECT * FROM Usuario")
            #note_list = cursor.fetchall()
            #print(len(note_list))
            #new_note = Note(note_list[0],new_note[1],new_note[2],note,nota,datetime.now()) #Schema

            cursor.execute("INSERT INTO Nota(nota_disciplina,descricao) VALUES (%s,%s)", (nota,note))
            connect.commit()
            cursor.close()

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