import SQLconnection
import os
from classes import Producto

def clearLinux():
    os.system('clear')

cursor = SQLconnection.db.cursor()

def buscarAutorProducto():
    sql = '''SELECT ID, NOMBRE FROM AUTOR WHERE NOMBRE LIKE %s '''
    nombre = str(input('Ingrese nombre autor: '))

    nombre = '%' + nombre + '%'

    cursor.execute(sql, (nombre, ))

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    pregunta = str(input('Desea buscar nuevamente?[S/n]: ')).upper()

    if pregunta == 'S':
        return True
    else:
        return False

def addAutorProducto(ident):
    sql = '''INSERT INTO AUTOR_PRODUCTO VALUES (%s, %s)'''

    cursor.execute('SELECT ID, NOMBRE FROM AUTOR ORDER BY NOMBRE')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    preguntaBuscar = str(input('Desea buscar autor?[S/n]: ')).upper()

    if preguntaBuscar == 'S':
        while buscarAutorProducto():
            continue    

    id_autor = int(input('Ingrese id de autor: '))

    clearLinux()

    val = (ident, id_autor)

    cursor.execute(sql, val)

    SQLconnection.db.commit()

    pregunta = str(input('Desea agregar otro autor?[S/n]: ')).upper()

    clearLinux()

    if pregunta == 'S':
        return True
    else:
        return False

def newProduct():
    clearLinux()
    ident = str(input('Ingrese id del producto: '))
    
    clearLinux()

    titulo = str(input('Ingrese el titulo del producto: '))

    clearLinux()
    cursor.execute('''SELECT * FROM TIPO_PRODUCTO''')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_tipo = int(input('Ingrese el id del tipo de producto: '))

    clearLinux()

    cursor.execute('''SELECT ID, NOMBRE FROM EDITORIAL''')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_editorial = int(input('Ingrese id de la editorial: '))

    clearLinux()
    desc = str(input('Ingrese descripcion del producto: '))

    clearLinux()
    producto = Producto(ident, id_tipo, id_editorial, desc, titulo)

    val = (producto.ident , producto.id_tipo , producto.id_editorial , producto.descripcion , producto.titulo)

    sql = '''INSERT INTO PRODUCTO VALUES (%s, %s, %s, %s, %s)'''

    cursor.execute(sql, val)

    SQLconnection.db.commit()

    while addAutorProducto(producto.ident):
        clearLinux()

newProduct()
