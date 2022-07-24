import bcrypt
import SQLconnection
from getpass import getpass
import os

def clearLinux():
    os.system('clear')

class Empleado:
    def __init__(self, rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido 
        self.id_bodega = id_bodega
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.id_cargo = id_cargo
        self.jefe = None

cursor = SQLconnection.db.cursor()

sql = 'INSERT INTO EMPLEADO(rut, nombre, id_bodega, usuario, contrasenia, apellido, id_cargo) VALUES (%s,%s,%s,%s,%s,%s,%s)'

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
empleado = Empleado(rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo)

val = (empleado.rut, empleado.nombre, empleado.id_bodega, empleado.usuario, empleado.contrasenia,empleado.apellido, empleado.id_cargo)

cursor.execute(sql, val)

SQLconnection.db.commit()
