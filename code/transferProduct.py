import SQLconnection
import os

def clearLinux():
    os.system('clear')

cursor = SQLconnection.db.cursor()
cursorDict = SQLconnection.db.cursor(dictionary=True)

def addRemoveProduct():

    sqlAdd = '''UPDATE PRODUCTO_BODEGA SET CANTIDAD = CANTIDAD + %s WHERE ID_PRODUCTO = %s AND ID_BODEGA = %s ;'''

    sqlRemove = '''UPDATE PRODUCTO_BODEGA SET CANTIDAD = CANTIDAD - %s WHERE ID_PRODUCTO = %s AND ID_BODEGA = %s ;'''

    producto = str(input('Ingrese id del producto: '))

    # obtener todas las bodegas en las que se encuentra el producto
    bodegas = []
    sqlBodegas=('''SELECT ID_BODEGA FROM PRODUCTO_BODEGA WHERE ID_PRODUCTO = %s''')
    cursorDict.execute(sqlBodegas, (producto, ))
    resultado = cursorDict.fetchall()
    for x in resultado:
        bodegas.append(int(x['ID_BODEGA']))
    #---------------

    cursorDict.execute('SELECT * FROM PRODUCTO_BODEGA')

    resultado = cursorDict.fetchall()
    print('Informacion del producto en bodegas:')
    for x in resultado:
        print(x)

    bodegaOrigen = int(input('Ingrese id de la bodega de origen: '))

    while bodegaOrigen not in bodegas:
        print('|... Producto no se encuentra en esta bodega...|')
        bodegaOrigen = int(input('Ingrese id de la bodega de origen: '))

    cantidad = int(input('Ingrese cantidad a transferir: '))

    bodegaDestino = int(input('Ingrese id de la bodega de destino: '))

    if bodegaDestino not in bodegas:
        sql = '''INSERT INTO PRODUCTO_BODEGA VALUES (%s, %s,%s)'''

        val = (producto, bodegaDestino, 0)

        cursor.execute(sql , val)

        SQLconnection.db.commit()

    val = (cantidad, producto, bodegaOrigen)

    cursor.execute(sqlRemove, val)

    SQLconnection.db.commit()

    val = (cantidad, producto, bodegaDestino)

    cursor.execute(sqlAdd, val)

    SQLconnection.db.commit()

addRemoveProduct()
