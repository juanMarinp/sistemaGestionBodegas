import SQLconnection
import addBodega
import newProduct
import time

def jefeMenu(opcion):

    if opcion == 1:
        bucle = True

        while bucle:
            addBodega.addBodega()

            pregunta = str(input('Desea ingresar otra bodega?[S/n]: ')).upper()

            if pregunta != 'S':
                bucle = False

    if opcion == 2:
        bucle = True
        while bucle:
            newProduct.newProduct()

            pregunta = str(input('Desea ingresar otro producto?[S/n]: ')).upper()

            if pregunta != 'S':
                bucle = False
    if opcion == 10:
        print('|... Hasta luego ...|')
        time.sleep(1)

