from Usuario import Usuario
from logger_base import log
from CursorDelPool import CursorDelPool

class UsuarioDao:

    _SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    _INSERTAR = "INSERT INTO usuario(username, password) VALUES(%s, %s)"
    _ACTUALIZAR = "UPDATE usuario SET username=%s, password=%s  WHERE id_usuario=%s"
    _ELIMINAR = "DELETE FROM usuario WHERE id_usuario=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for i in registros:
                usuario = Usuario(i[0], i[1], i[2])
                usuarios.append(usuario)
        return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Usuario insertado: {usuario}")
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Usuario actualizado: {usuario}")
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Usuario eliminado: {usuario}")
            return cursor.rowcount

#Zona de pruebas
if __name__ == "__main__":
    #Insertar un registro
    #usuario_1 = Usuario(username="jwulleny", password=789)
    #usuarios_insertados = UsuarioDao.insertar(usuario_1)
    #log.debug(f"Usuario insertado: {usuarios_insertados}")

    #Actualizar un registro
    #usuario_1 = Usuario(2, "tamyg", 654)
    #usuarios_insertados = UsuarioDao.actualizar(usuario_1)
    #log.debug(f"Usuario actualizado: {usuarios_insertados}")

    #Eliminar un registro
    #usuario_1 = Usuario(4)
    #usuarios_eliminados = UsuarioDao.eliminar(usuario_1)
    #log.debug(f"Usuario eliminado: {usuarios_eliminados}")

    #Seleccionar un registro
    usuarios = UsuarioDao.seleccionar()
    for i in usuarios:
        log.debug(i)