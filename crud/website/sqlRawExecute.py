import sqlite3
from sqlite3 import OperationalError


def executeScriptsFromFile(sqlFile,cursor):
    fd = open(sqlFile,'r')
    sqlFile = fd.read()

    fd.close()

    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            cursor.execute(command)
        except OperationalError as msg:
            print("Comando Skipado",msg)
