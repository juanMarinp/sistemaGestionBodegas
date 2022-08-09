import SQLconnection
import os

def clearLinux():
    os.system('clear')

cursor = SQLconnection.db.cursor()

def addRemoveProduct():

    sqlAdd = '''UPDATE PRODUCTO_BODEGA SET CANTIDAD = CANTIDAD + %s WHERE ID_PRODUCTO = %s AND ID_BODEGA = %s ;'''

    sqlRemove = '''UPDATE PRODUCTO_BODEGA SET CANTIDAD = CANTIDAD - %s WHERE ID_PRODUCTO = %s AND ID_BODEGA = %s ;'''

    producto = str(input('Ingrese id del producto: '))

    bodegaOrigen = int(input('Ingrese id de la bodega de origen: '))

    cantidad = int(input('Ingrese cantidad a transferir: '))

    bodegaDestino = int(input('Ingrese id de la bodega de destino: '))

    val = (cantidad, producto, bodegaOrigen)

    cursor.execute(sqlRemove, val)

    SQLconnection.db.commit()

    val = (cantidad, producto, bodegaDestino)

    cursor.execute(sqlAdd, val)

    SQLconnection.db.commit()


addRemoveProduct()
