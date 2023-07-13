from . import db 
import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy.sql import func

# TABLES do Banco de Dados
class Note(db.Model):
    id = sa.Column(sa.Integer,primary_key=True)
    mat = sa.Column(sa.Integer,primary_key=True,unique=True)
    nome = sa.Column(sa.String(150))
    data = sa.Column(sa.String(10000)) # 20000 caracteres
    date = sa.Column(sa.DateTime(timezone=True),default=func.now())
    user_id = sa.Column(sa.Integer,sa.ForeignKey("user.id")) 

class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer,primary_key=True) # INT PK
    mat = sa.Column(sa.Integer,unique=True)
    email = sa.Column(sa.String(150),unique=True) #VARCHAR(150) UN
    nome = sa.Column(sa.String(150)) # VARCHAR(150) UN
    curso = sa.Column(sa.String(150))
    password = sa.Column(sa.String(150)) #VARCHAR(150) UN
    notes = db.relationship('Note') # INSERT INTO user
    
class Course(db.Model):
    id = sa.Column(sa.Integer,primary_key=True)
    cod = sa.Column(sa.String(7),primary_key=True)
    nome = sa.Column(sa.String(150))
    cod_depto = sa.Column(sa.String(),sa.ForeignKey('department.cod'))


class Department(db.Model):
    id = sa.Column(sa.Integer,primary_key=True)
    cod = sa.Column(sa.String(3),primary_key=True)
    courses = db.relationship('Course')

class Classroom(db.Model):
    id = sa.Column(sa.Integer,primary_key=True)
    cod_course = sa.Column(sa.String(7),sa.ForeignKey('course.cod'))
    cod_depto = sa.Column(sa.String(3),sa.ForeignKey('department.cod'))