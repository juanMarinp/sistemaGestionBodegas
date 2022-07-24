import SQLconnection 
import bcrypt
import os
from getpass import getpass
import login
import newUser

print(login.login())

'''
access = False

if login.login():
    print('|...Contraseña correcta...|')
    access = True
else:
    print('|...Contraseña o usuario incorrectos...|')
    access = False

#newUser.newUser()

'''
