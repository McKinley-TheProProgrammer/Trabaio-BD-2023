import psycopg2
from sqlite3 import OperationalError
import csv



# STRINGS COM QUERYS DO SQL PURO
INSERT_USER_RETURNING_MAT = "IF NOT EXISTS (SELECT * FROM Usuario WHERE matricula = %s AND email = %s) BEGIN INSERT INTO Usuario(matricula,nome,email,senha,curso) VALUES (%s,%s,%s,%s,%s) RETURNING id;"

INSERT_AVAILABLE_DISCIPLINES = "INSERT INTO Disciplina(cod_disciplina,nome,codigo_depto) VALUES (%s,%s,%s) RETURNING id;"

INSERT_NOTAS_RETURNING = "INSERT INTO Nota(nota_disciplina,descricao) VALUES (%s,%s) RETURNING id;"

LOGIN_USER = "SELECT * FROM Usuario WHERE email=%s AND senha=%s LIMIT 1;"

SELECT_USERS = "SELECT * FROM Usuario;"
SELECT_USER_FROM_ID = "SELECT * FROM Usuario WHERE id=%s LIMIT 1;"
SELECT_TURMA_FROM_ID = "SELECT * FROM Turma WHERE id=%s LIMIT 1;"

SELECT_NOTES = "SELECT * FROM Nota;"
SELECT_TURMAS = "SELECT * FROM Turma;"
SELECT_DEPARTAMENTOS = "SELECT * FROM Departamento;"
SELECT_DISCIPLINAS = "SELECT * FROM Disciplina;"

DELETE_USER_BY_ID = "DELETE FROM Usuario WHERE id=%s;"



def executeScriptsFromFile(sqlFile,cursor):
    fd = open(sqlFile,'r')
    sqlFile = fd.read()

    fd.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except psycopg2.Error as msg:
            print(f"Comando de {command} Skipado",msg)

    return True

def dropAllTables(conn):
    executeScriptsFromFile("sql_querys/deletarTabelas.sql",conn)



def get_usuario(id : int):
    from .auth import get_db_connection
    connect = get_db_connection()
    with connect:
        with connect.cursor() as cursor:
            cursor.execute(SELECT_USER_FROM_ID,(id,))
            user = cursor.fetchone()
            print(user)
    
    return user

def get_turma(id : int):
    from .auth import get_db_connection
    connect = get_db_connection()
    with connect:
        with connect.cursor() as cursor:
            cursor.execute(SELECT_TURMA_FROM_ID,(id,))
            turma = cursor.fetchone()
            print(turma)
    
    return turma

def get_courses():
    from .auth import get_db_connection
    connect = get_db_connection()
    with connect:
        with connect.cursor() as cursor:
            cursor.execute(SELECT_DISCIPLINAS)
            turmas = cursor.fetchall()
            
    return turmas

