import bcrypt
import SQLconnection
import os
from getpass import getpass
import json

cursor = SQLconnection.db.cursor()

def login():
    usuario = str(input('Ingrese usuario: '))

    sql = '''SELECT USUARIO FROM EMPLEADO WHERE USUARIO = (%s)'''

    cursor.execute(sql, (usuario, ))

    resultado = cursor.fetchone()

    if resultado != None :
        sql = ('''SELECT CONTRASENIA FROM EMPLEADO WHERE USUARIO = (%s) ''')

        contrasenia = getpass('Ingrese contraseña: ')

        cursor.execute(sql, (usuario, ))

        resultado = cursor.fetchone()

        p = resultado[0]

        return bcrypt.checkpw(contrasenia.encode('UTF-8'), p.encode('UTF-8'))

    else:
        contrasenia = getpass('Ingrese contraseña: ')
        return False
