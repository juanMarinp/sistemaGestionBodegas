import SQLconnection
import os
from classes import Producto

cursor = SQLconnection.db.cursor()

def addAutorProducto(ident):
    sql = '''INSERT INTO AUTOR_PRODUCTO VALUES (%s, %s)'''

    cursor.execute('SELECT ID, NOMBRE FROM AUTOR')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_autor = int(input('Ingrese id de autor'))

    val = (ident, id_autor)

    cursor.execute(sql, val)

    SQLconnection.db.commit()

    pregunta = str(input('Desea agregar otro autor?[S/n]')).upper()

    if pregunta == 'S':
        return True
    else:
        return False

def newProduct():
    ident = str(input('Ingrese id del producto: '))

    titulo = str(input('Ingrese el titulo del producto: '))

    cursor.execute('''SELECT * FROM TIPO_PRODUCTO''')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_tipo = int(input('Ingrese el id del tipo de producto: '))


    cursor.execute('''SELECT ID, NOMBRE FROM EDITORIAL''')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    id_editorial = int(input('Ingrese id de la editorial: '))

    desc = str(input('Ingrese descripcion del producto: '))


    cursor.execute('''SELECT * FROM BODEGA''')

    resultado = cursor.fetchall()

    for x in resultado:
        print(x)
    
    id_bodega = int(input('Ingrese id de la bodega: '))

    producto = Producto(ident, id_tipo, id_editorial, desc, id_bodega, titulo)

    val = (producto.ident , producto.id_tipo , producto.id_editorial , producto.descripcion , producto.id_bodega, producto.titulo)

    sql = '''INSERT INTO PRODUCTO VALUES (%s, %s, %s, %s, %s, %s)'''

    cursor.execute(sql, val)

    SQLconnection.db.commit()

    while addAutorProducto(producto.ident):
        cleanLinux()

newProduct()
