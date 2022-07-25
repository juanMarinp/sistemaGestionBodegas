import SQLconnection 
import bcrypt
import os
from getpass import getpass
import login
import newUser

access = False
accessContador = 0

while access == False:
    if login.login():
        print('|...Contraseña correcta...|')
        access = True
    else:
        print('|...Contraseña o usuario incorrectos...|')
        access = False
        accessContador += 1
    if accessContador == 3:
        print('|...Ha excedido el máximo de intentos...|')
        break
