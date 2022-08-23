import SQLconnection
import os

cursor = SQLconnection.db.cursor()

def buscarProductos():
    sql = '''SELECT ID, TITULO FROM PRODUCTO WHERE TITULO LIKE %s'''
    nombre = str(input('Ingrese nombre del producto: '))

    nombre = '%' + nombre + '%'

    cursor.execute(sql, (nombre ,))

    resultado = cursor.fetchall()

    for x in resultado:
        return print(x)

def buscarProductosFlujo():
    buscarProductos()

    pregunta = str(input('Desea buscar otro producto?[S/n]: ')).upper()
    if pregunta == 'S':
        return True
    else:
        return False

def addProductoBodega():

    sql = '''INSERT INTO PRODUCTO_BODEGA VALUES (%s, %s, %s)'''

    cursor.execute('SELECT ID, TITULO FROM PRODUCTO')
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

    pregunta = str(input('Desea buscar un producto?[S/n]: ')).upper()

    if pregunta == 'S':
        while buscarProductosFlujo():
            continue

    id_producto = str(input('Ingrese id del producto: '))

    cursor.execute('SELECT ID, CALLE FROM BODEGA')
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

    id_bodega = int(input('Ingrese id de la bodega: '))

    cantidad = int(input('Ingrese cantidad de producto: '))

    val = (id_producto, id_bodega, cantidad)

    cursor.execute(sql, val)

    SQLconnection.db.commit()

addProductoBodega()
