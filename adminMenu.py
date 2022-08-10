import newUser
import time


def adminMenu(opcion):

    if opcion == 1:
    
        bucle = True

        while bucle:

            newUser.newUser()

            pregunta = str(input('Desea ingresar otro usuario?[S/n]: ')).upper()

            if pregunta != 'S':
                bucle = False
    if opcion == 10:
        print('|... Hasta luego ...|')
        time.sleep(1)
