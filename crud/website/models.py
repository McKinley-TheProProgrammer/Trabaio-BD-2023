from . import db 
import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy.sql import func

# TABLES do Banco de Dados

# CREATE TABLE notas (....)
class Note():

    def __init__(self,id,mat,nome,desc,date,user_id):
        self.id = id
        self.data = desc
        self.date = date
        self.mat = mat
        self.nome = nome
        self.user_id = user_id # INT FOREIGN KEY REFERENCES User(user.id)

# CREATE TABLE user (....)
class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer,primary_key=True) # INT PRIMARY KEY
    mat = sa.Column(sa.Integer,unique=True) # INT UN
    email = sa.Column(sa.String(150),unique=True) #VARCHAR(150) UN
    nome = sa.Column(sa.String(150)) # VARCHAR(150) UN
    curso = sa.Column(sa.String(150)) # VARCHAR(150)
    password = sa.Column(sa.String(150)) #VARCHAR(150) UN
    notes = db.relationship('Note') # INSERT INTO user
    
# CREATE TABLE disciplina (....)
class Course(db.Model):
    id = sa.Column(sa.Integer,primary_key=True) # INT PRIMARY KEY
    cod = sa.Column(sa.String(7),primary_key=True) # VARCHAR(7) PRIMARY KEY
    nome = sa.Column(sa.String(150)) # VARCHAR(150)
    cod_depto = sa.Column(sa.String(3),sa.ForeignKey('department.cod')) # INT FOREIGN KEY REFERENCES Department(department.cod)

# CREATE TABLE departamento (....)
class Department(db.Model):
    id = sa.Column(sa.Integer,primary_key=True) # INT PRIMARY KEY
    cod = sa.Column(sa.String(3),primary_key=True) # VARCHAR(150) PRIMARY KEY
    courses = db.relationship('Course')

# CREATE TABLE turma (....)
class Classroom(db.Model):
    id = sa.Column(sa.Integer,primary_key=True) # INT PRIMARY KEY
    cod_course = sa.Column(sa.String(7),sa.ForeignKey('course.cod')) # VARCHAR(7) FOREIGN KEY REFERENCES Course(Course.cod)
    cod_depto = sa.Column(sa.String(3),sa.ForeignKey('department.cod')) # VARCHAR(3) FOREIGN KEY REFERENCES Department(department.cod)