import bcrypt
import SQLconnection
from getpass import getpass
import os
from classes import Jefe, Bodeguero
from itertools import cycle
import time

def obtenerUsuarios():
    arrUsuarios = []

    cursor.execute('SELECT USUARIO FROM EMPLEADO')

    resultado = cursor.fetchall()

    for x in resultado:
        arrUsuarios.append(x['USUARIO'])

    return arrUsuarios

def validarUsuario(usuario):
    if usuario in obtenerUsuarios():
        print('|....Nombre usuario ya existe....|')
        validacion = False
        time.sleep(1)
        clearLinux()
    else:
        validacion = True

    return validacion

'''Funcion para obtener digito verificador del rut'''
def digitoVerificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    return (-s) % 11
'''Funcion para limpiar la consola en linux'''
def clearLinux():
    os.system('clear')

cursor = SQLconnection.db.cursor(dictionary=True)

def newUser():

    rutValido = False

    while rutValido != True:

        clearLinux()
        rut = int(input('Ingrese rut(8 primeros digitos sin puntos): '))

        digitoV = str(digitoVerificador(rut))

        clearLinux()

        rutDV = str(input('Ingrese rut (último digito): '))

        clearLinux()
        if digitoV != rutDV :
            print('|....Rut no valido....|')
            time.sleep(1)
            rutValido = False
        else:
            print('|....Rut valido....|')
            rutValido = True
            time.sleep(1)

    if rutValido:

        clearLinux()

        rut = str(rut) + '-' + digitoV

        nombre = str(input('Ingrese nombre: '))

        clearLinux()
        apellido = str(input('Ingrese apellido: '))

        clearLinux()
        cursor.execute('select ID, CALLE from BODEGA')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        id_bodega = int(input('Ingrese id bodega: '))

        clearLinux()

        usuario = str(input('Ingrese nombre usuario: ')).lower()

        while (validarUsuario(usuario) == False):
            print('|...Vuelva a intentar...|')
            time.sleep(1)
            usuario = str(input('Ingrese nombre usuario: ')).lower()

        clearLinux()
        contrasenia = getpass('Ingrese contraseña: ')

        clearLinux()
        contrasenia = bcrypt.hashpw(contrasenia.encode('UTF-8'), bcrypt.gensalt())

        cursor.execute('select * from CARGO')

        resultado = cursor.fetchall()

        for x in resultado:
            print(x)

        id_cargo = int(input('Ingrese id de cargo: '))

        if id_cargo == 2 or id_cargo == 1:

            sql = 'INSERT INTO EMPLEADO(rut, nombre, id_bodega, usuario, contrasenia, apellido, id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            clearLinux()
            jefe = Jefe(rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo)

            val = (jefe.rut, jefe.nombre, jefe.id_bodega, jefe.usuario, jefe.contrasenia, jefe.apellido, jefe.id_cargo)

            cursor.execute(sql, val)

            SQLconnection.db.commit()
        else: 
            cursor.execute('''SELECT RUT, NOMBRE, APELLIDO FROM EMPLEADO WHERE ID_CARGO = 2''')
            
            resultado = cursor.fetchall()

            for x in resultado:
                print(x)

            id_jefe = str(input('Ingrese rut jefe: '))
            bodeguero = Bodeguero(rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo, id_jefe)

            sql = 'INSERT INTO EMPLEADO(rut, nombre,rut_jefe, id_bodega, usuario, contrasenia, apellido, id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'

            val = (bodeguero.rut, bodeguero.nombre,bodeguero.id_jefe, bodeguero.id_bodega, bodeguero.usuario, bodeguero.contrasenia, bodeguero.apellido, bodeguero.id_cargo)
            cursor.execute(sql, val)

            SQLconnection.db.commit()
