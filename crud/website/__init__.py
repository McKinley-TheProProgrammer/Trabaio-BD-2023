from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
import psycopg2

from .sqlRawExecute import executeScriptsFromFile

from dotenv import load_dotenv




db = SQLAlchemy()

DB_NAME = "database.db"

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
            executeScriptsFromFile("sql_querys/criacaotabelassql.sql",cursor)
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

