import SQLconnection
import os

cursor = SQLconnection.db.cursor()

def addProductoBodega():

    sql = '''INSERT INTO PRODUCTO_BODEGA VALUES (%s, %s, %s)'''

    id_producto = str(input('Ingrese id del producto: '))

    id_bodega = int(input('Ingrese id de la bodega: '))

    cantidad = int(input('Ingrese cantidad de producto: '))

    val = (id_producto, id_bodega, cantidad)

    cursor.execute(sql, val)

    SQLconnection.db.commit()
