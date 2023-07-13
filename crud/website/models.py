from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    data = db.Column(db.String(20000)) # 20000 caracteres
    date = db.Column(db.DateTime(timezone=True),default=func.now())
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) # FK 
    #user_name = db.Column(db.String(150),db.ForeignKey("user.nome"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True) # INT PK
    email = db.Column(db.String(150),unique=True) #VARCHAR(150) UN
    nome = db.Column(db.String(150)) # VARCHAR(150) UN
    curso = db.Column(db.String(150))
    password = db.Column(db.String(150)) #VARCHAR(150) UN
    notes = db.relationship('Note') # INSERT INTO user
    

class Course(db.Model):
    cod = db.Column(db.String(6),primary_key=True)