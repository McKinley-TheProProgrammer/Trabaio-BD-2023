from flask import Blueprint, render_template,request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note

import json

views = Blueprint('views',__name__)

# CREATE VIEW home ()
@views.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if(len(note) < 1):
            flash('Avaliação muito pequena!!', category='error')
        else:
            new_note = Note() #Schema
            #db.session.add(new_note)
            #db.session.commit()
            flash('Avaliação Enviada', category='success')

    return render_template("home.html",user=current_user)

@views.route('/delete-note',methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            #db.session.delete(note)
            #db.session.commit()
            return jsonify({})