import bcrypt
import SQLconnection
import os
from getpass import getpass

cursor = SQLconnection.db.cursor()

sql = ('''SELECT CONTRASENIA FROM EMPLEADO WHERE USUARIO = (%s) ''')

usuario = str(input('Ingrese usuario: '))

contrasenia = getpass('Ingrese contraseña: ')

cursor.execute(sql, (usuario, ))

resultado = cursor.fetchone()

p = resultado[0]

if bcrypt.checkpw(contrasenia.encode('UTF-8'), p.encode('UTF-8')):
    print('it matches!')
else:
    print('it doesnt!')


