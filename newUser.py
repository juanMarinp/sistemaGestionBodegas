import bcrypt
import SQLconnection
from getpass import getpass
import os
from classes import Jefe

def clearLinux():
    os.system('clear')

cursor = SQLconnection.db.cursor()

sql = 'INSERT INTO EMPLEADO(rut, nombre, id_bodega, usuario, contrasenia, apellido, id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s)'

def newUser():
    rut = str(input('Ingrese rut: '))

    clearLinux()

    nombre = str(input('Ingrese nombre: '))

    clearLinux()
    apellido = str(input('Ingrese apellido: '))

    clearLinux()
    cursor.execute('select * from BODEGA')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_bodega = int(input('Ingrese id bodega: '))

    clearLinux()
    usuario = str(input('Ingrese nombre de usuario: '))

    clearLinux()
    contrasenia = getpass('Ingrese contraseña: ')

    clearLinux()
    contrasenia = bcrypt.hashpw(contrasenia.encode('UTF-8'), bcrypt.gensalt())

    cursor.execute('select * from CARGO')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_cargo = int(input('Ingrese id de cargo: '))

    clearLinux()
    jefe = Jefe(rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo)

    val = (jefe.rut, jefe.nombre, jefe.id_bodega, jefe.usuario, jefe.contrasenia, jefe.apellido, jefe.id_cargo)

    cursor.execute(sql, val)

    SQLconnection.db.commit()
