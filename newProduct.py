import SQLconnection
import os

cursor = SQLconnection.db.cursor()

def newProduct():
    ident = str(input('Ingrese id del producto: '))

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

newProduct()
