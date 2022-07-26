class Jefe:
    def __init__(self, rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.id_bodega = id_bodega
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.id_cargo = id_cargo

class Bodeguero:
    def __init__(self, rut, nombre, apellido, id_bodega, usuario, contrasenia, id_cargo, id_jefe):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.id_bodega = id_bodega
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.id_cargo = id_cargo
        self.id_jefe = id_jefe

class Producto:
    def __init__(self, ident, id_tipo, id_editorial, descripcion, titulo):
        self.ident = ident
        self.id_tipo = id_tipo
        self.id_editorial = id_editorial
        self.descripcion = descripcion
        self.titulo = titulo
