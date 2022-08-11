import SQLconnection
from classes import Bodega

cursor = SQLconnection.db.cursor()

def addBodega():

    calle = str(input('Ingrese nombre de la calle con numero: '))
    
    cursor.execute('SELECT * FROM COMUNA')
    resultado = cursor.fetchall()
    for x in resultado:
        print(x)

    id_comuna = int(input('Ingrese id de la comuna: '))

    bodega = Bodega(calle, id_comuna)

    val = (bodega.calle, bodega.ident_comuna)

    sql = ('''INSERT INTO BODEGA (CALLE, ID_COMUNA) VALUES (%s, %s)''')

    cursor.execute(sql, val)

    SQLconnection.db.commit()
