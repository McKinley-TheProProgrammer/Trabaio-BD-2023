import psycopg2
from sqlite3 import OperationalError
import csv

def executeScriptsFromFile(sqlFile,cursor):
    fd = open(sqlFile,'r')
    sqlFile = fd.read()

    fd.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except psycopg2.Error as msg:
            print("Comando Skipado",msg)

    return True

def dropAllTables(conn):
    executeScriptsFromFile("sql_querys/deletarTabelas.sql",conn)


# STRINGS COM QUERYS DO SQL PURO
INSERT_USER_RETURNING_MAT = "INSERT INTO Usuario(matricula,nome,email,senha,curso) VALUES (%s,%s,%s,%s,%s) RETURNING id;"

INSERT_AVAILABLE_DISCIPLINES = "INSERT INTO Disciplina(cod_disciplina,nome,codigo_depto) VALUES (%s,%s,%s) RETURNING id;"

INSERT_NOTAS_RETURNING = "INSERT INTO Nota(nota_disciplina,descricao) VALUES (%s,%s) RETURNING id;"

LOGIN_USER = "SELECT * FROM Usuario WHERE email = %s AND senha = %s LIMIT 1;"