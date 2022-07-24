import SQLconnection 

cursor = SQLconnection.db.cursor()

cursor.execute('SELECT * FROM COMUNA')

resultado = cursor.fetchall()

for x in resultado:
    print(x)
