from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    mat = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    data = db.Column(db.String(20000)) # 20000 caracteres
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_mat = db.Column(db.Integer,db.ForeignKey("user.mat")) # FK 
    user_name = db.Column(db.String(150),db.ForeignKey("user.nome"))

class User(db.Model, UserMixin):
    mat = db.Column(db.Integer,primary_key=True) # INT PK
    nome = db.Column(db.String(150)) # VARCHAR(150) UN
    curso = db.Column(db.String(6))
    email = db.Column(db.String(150),unique=True) #VARCHAR(150) UN
    password = db.Column(db.String(150)) #VARCHAR(150) UN
    notes = db.relationship("Note") # INSERT INTO user
    

class Course(db.Model):
    cod = db.Column(db.String(6),primary_key=True)