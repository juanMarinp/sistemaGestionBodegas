import SQLconnection 
import bcrypt
import os
from getpass import getpass
import login
import newUser
import adminMenu
import jefeMenu

cursor = SQLconnection.db.cursor(dictionary=True)

access = False
accessContador = 0

while access == False:
    usuario = str(input('Ingrese nombre de usuario: '))
    if login.login(usuario):
        print('|...Contraseña correcta...|')
        access = True
    else:
        print('|...Contraseña o usuario incorrectos...|')
        access = False
        accessContador += 1
    if accessContador == 3:
        print('|...Ha excedido el máximo de intentos...|')
        break

sql = ('''SELECT CARGO.NOMBRE FROM CARGO JOIN EMPLEADO ON EMPLEADO.ID_CARGO = CARGO.ID WHERE USUARIO = %s''')

cursor.execute(sql, (usuario, ))

resultado = cursor.fetchone()

cargo = resultado['NOMBRE']

if cargo == 'ADMIN':

    bucle = True

    while bucle:

        print('|------- Menú -------|')

        print('(1) Añadir usuario')
        print('(2) Editar usuario')
        print('(9) Eliminar usuario')
        print('(10) Salir')

        opcion = int(input('Ingrese número opción: '))

        adminMenu.adminMenu(opcion)

        if opcion == 10:
            bucle = False

if cargo == 'JEFE':

    bucle = True

    while bucle:

        print('|------- Menú -------|')

        print('(1) Añadir bodega')
        print('(2) Añadir producto')
        print('(10) Salir')

        opcion = int(input('Ingrese número opción: '))

        jefeMenu.jefeMenu(opcion)

        if opcion == 10:
            bucle = False
