from flask import Blueprint, render_template, request, flash, redirect, url_for

from werkzeug.security import generate_password_hash, check_password_hash
import os, psycopg2, csv

from flask_login import login_user, login_required, logout_user
from .sqlRawExecute import *

INSERT_USER_RETURNING_MAT = "INSERT INTO Usuario(matricula,nome,email,senha,curso) VALUES (%s,%s,%s,%s,%s) RETURNING matricula"

INSERT_AVAILABLE_DISCIPLINES = "INSERT INTO Disciplina(cod_disciplina,nome,codigo_depto) VALUES (%s) RETURNING id"

INSERT_NOTAS_RETURNING = "INSERT INTO Nota(usuario_id,nota_disciplina,matricula,nome,descricao,dataDePostagem) VALUES (%s)"

auth = Blueprint('auth',__name__)

def get_db_connection():
    url = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(url)
    return conn

connect = get_db_connection()
#cursor = connect.cursor()

@auth.route("/login",methods=['GET','POST'])
def login():
    global loggedIn
    if(request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')

        print([email,password])
        with connect.cursor() as cursor:
            cursor.execute(LOGIN_USER,(email,password))
            user = cursor.fetchone()
            print(user)
            if(user):
                #print(user.password)
                if(user[4] == password):
                    flash('Logado',category='success')
                    #login_user(user, remember=True)
                    loggedIn = True
                    return redirect(url_for('views.home'))
                else:
                    flash('Senha incorreta, tente novamente', category='error')
            else:
                flash('Email não existe', category='error')

    return render_template("login.html")

@auth.route('/logout',methods=['GET'])
def logout():
    loggedIn = False
    logout_user()
    conn = get_db_connection()
    cursor = conn.cursor()

    id = request.form.get('id')
    print(id)
    cursor.execute(DELETE_USER_BY_ID,(id,))

    conn.commit()

    cursor.close()
    conn.close()

    flash("Usuario Deslogado com sucesso", category="success")

    return redirect(url_for('views.home'))

@auth.route('/index-turmas', methods=['GET','POST'])
def index_turmas():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(SELECT_TURMAS)

    turmas = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index-turmas.html',classes=turmas)

@auth.route('/index-disciplinas', methods=['GET','POST'])
def index_disciplinas():
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(SELECT_DISCIPLINAS)

    disciplinas = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('index-disciplinas.html',disciplines=disciplinas)


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    global loggedIn
    global user_id
    if request.method == 'POST':
            mat = request.form.get('mat')
            email = request.form.get('email')
            nome = request.form.get('nome')
            curso = request.form.get('curso')
            password1 = request.form.get('password1')
            password2 = request.form.get('password2')

            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(SELECT_USERS)
            user = cursor.fetchone()
            conn.commit()
            #current_user = user
            if user != None:
                flash('Usuário já existe.', category='error')
            elif len(email) < 4:
                flash('Email precisa ter no minimo 4 caracteres.', category='error')
            elif len(nome) < 2:
                flash('Nome precisa ter no minimo 2 caracteres', category='error')
            elif len(curso) < 8:
                flash('Curso precisa ter no minimo 8 caracteres', category='error')
            elif password1 != password2:
                flash('As senhas não são iguais', category='error')
            elif len(password1) < 7:
                flash('A senha precisa ter no minimo 8 caracteres', category='error')
            else:
                cursor.execute(INSERT_USER_RETURNING_MAT,(mat,nome,email,password1,curso))
                cursor.execute(LOGIN_USER,(email,password1))
                user = cursor.fetchone()
                conn.commit()
                
                cursor.close()
                conn.close()
                #db.session.add(new_user)
                #db.session.commit()
                
                #login_user(new_user, remember=True)
                flash('Conta Registrada!', category='success')
                return redirect(url_for('views.home'))
            
    return render_template("sign_up.html",us = user)