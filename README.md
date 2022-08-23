# sistemaGestionBodegas

paquetes instalados:

pip install mysql-connector-python

pip install bcrypt

Problematica a resolver:

Listado de productos y bodegas de una librería

La librería “El gran Poeta”, para la organización de sus sucursales, requiere de un sistema que permita visualizar un listado de productos en cada una de las bodegas que esta empresa posee.

El sistema por realizar es una primera aproximación a un sistema de inventario, considerando las siguientes funcionalidades esperadas por el cliente:

1.	Se deberán poder crear productos en el inventario.

a.	Los productos podrán ser:

i.	Libros

ii.	Revistas

iii.	Enciclopedias

b.	Se deberá reconocer a cada producto, la editorial y el o los autores relacionados.
c.	Se deberá poder agregar una breve descripción o resumen del producto.
2.	Se deberán gestionar las bodegas existentes en la organización, identificando de forma única cada una de ellas.
3.	Se deberá poder agregar o sacar productos de las bodegas, generándose un documento de movimiento, en donde se detalle:
a.	Bodega origen
b.	Bodega destino
c.	Lista de productos y sus cantidades
4.	Se deberá proveer una previsualización del documento de movimiento de productos de bodega, en donde se observe:
a.	Bodega de origen
b.	Bodega de destino
c.	Lista de productos y sus cantidades
d.	Usuario que realiza la operación
5.	Solo el jefe de bodega podrá crear bodegas y productos.
6.	Solo el bodeguero podrá realizar los movimientos de productos de una bodega a otra.
7.	No existirá un bodeguero que a la vez sea jefe de bodegas, es decir son perfiles separados.
8.	Para ingresar al sistema, se deberá solicitar un usuario y contraseña; y el sistema deberá determinar el perfil del usuario que ingresa de acuerdo con los registros contenidos en la base de datos.
9.	Deberá existir un registro de editoriales antes de crear los productos.
10.	Para esta primera versión, los autores en los productos podrán ser ingresados ya sea desde un mantenedor específico o agregados a mano.
11.	Deberá poder identificarse de forma única cada uno de los movimientos de bodega generados, identificando el usuario que realizó dicho movimiento.
12.	El jefe de bodega podrá generar un informe en donde se indique:
a.	Cantidad de productos por bodega
b.	Tipos de productos (revistas, libros o enciclopedias)
c.	Listar solo los productos de una bodega por una editorial específica.
13.	Se deberá poder generar un informe de todos los movimientos de bodega, en donde se indiquen:
a.	Fecha del movimiento
b.	Bodega de origen
c.	Bodega de destino
d.	Usuario que realiza el movimiento
14.	Todos los informes el usuario jefe de bodega será el único que podrá obtenerlos.
15.	No se podrán eliminar bodegas con productos en ella
16.	No se podrán eliminar productos si estos ya se encuentran registrados en una bodega.
17.	No se podrán eliminar editoriales o autores, si estos tienen libros asignados.
