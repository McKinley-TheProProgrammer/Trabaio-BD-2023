from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
import psycopg2
import csv

from .sqlRawExecute import executeScriptsFromFile, dropAllTables

from dotenv import load_dotenv


db = SQLAlchemy()

DB_NAME = "database.db"

deptos = 'data/2023.1/departamentos_2023-1.csv'
disciplinas = 'data/2023.1/disciplinas_2023-1.csv'
turmas = 'data/2023.1/turmas_2023-1.csv'

#Criação do Aplicativo
def create_app():
    load_dotenv()
    app = Flask(__name__)
    url = os.getenv("DATABASE_URL")
    connection = psycopg2.connect(url)

    
    app.config['SECRET_KEY'] = 'KEY_SECRETO'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note

    #data = request.get_json()
    #name = data["name"]
    with connection:
        with connection.cursor() as cursor:
            dropAllTables(cursor)
            executeScriptsFromFile("sql_querys/criacaotabelassql.sql",cursor)

            
            with open(disciplinas, 'r',encoding='utf8') as csvfile:
                i = 0
                csvreader = csv.reader(csvfile)
            
                next(csvreader)

                for line in csvreader:
                    if(i > 50):
                        break
                    try:
                        #print(line)
                        cursor.execute("INSERT INTO Disciplina (cod_disciplina,nome,codigo_depto) VALUES (%s,%s,%s)", (line[0],line[1],line[2]))
                        
                    except UnicodeDecodeError as erro:
                        print(erro)
                    i += 1
                

            cursor.close()
            connection.commit()
    #with app.app_context():
    #    print("Criando as Tabelas do BD")
    #    db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    

    return app

