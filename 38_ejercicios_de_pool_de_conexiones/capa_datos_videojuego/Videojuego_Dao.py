from Videojuego import Videojuego
from Conexion import Conexion
from logger_base import log
from Cursor_del_pool import Cursor_Del_Pool

class Videojuego_Dao:

    _SELECCIONAR = "SELECT * FROM videojuegos ORDER BY id_videojuego"
    _INSERTAR = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
    _ACTUALIZAR = "UPDATE videojuegos SET nombre=%s, genero=%s, desarrolladora=%s, plataforma=%s, año=%s  WHERE id_videojuego=%s"
    _ELIMINAR = "DELETE FROM videojuegos WHERE id_videojuego=%s"

    @classmethod
    def seleccionar(cls):
        with Cursor_Del_Pool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            videojuegos = []
            for i in registros:
                videojuego = Videojuego(i[0], i[1], i[2], i[3], i[4], i[5])
                videojuegos.append(videojuego)
        return videojuegos

    @classmethod
    def insertar(cls, videojuego):
        with Cursor_Del_Pool() as cursor:
            valores = (videojuego.nombre, videojuego.genero, videojuego.desarrolladora, videojuego.plataforma, videojuego.año)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Videojuego insertado: {videojuego}")
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, videojuego):
        with Cursor_Del_Pool() as cursor:
            valores = (videojuego.nombre, videojuego.genero, videojuego.desarrolladora, videojuego.plataforma, videojuego.año, videojuego.id_videojuego)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Videojuego actualizado: {videojuego}")
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, videojuego):
        with Cursor_Del_Pool() as cursor:
            valores = (videojuego.id_videojuego,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f"Videojuego eliminado: {videojuego}")
            return cursor.rowcount

if __name__ == "__main__":
    #Insertar un registro
    videojuego_1 = Videojuego(nombre="Yoshi's Island", genero="Plataformas", desarrolladora="Nintendo", plataforma="SNES", año=1995)
    videojuegos_insertados = Videojuego_Dao.insertar(videojuego_1)
    log.debug(f"Videojuego insertado: {videojuegos_insertados}")

    #Actualizar un registro
    videojuego_1 = Videojuego(1, "Resident Evil: Code: Veronica", "Survival Horror", "Capcom", "Dreamcast", 2000)
    videojuegos_actualizados = Videojuego_Dao.actualizar(videojuego_1)
    log.debug(f"Videojuego actualizado: {videojuegos_actualizados}")

    #Eliminar un registro
    videojuego_1 = Videojuego(15)
    videojuegos_eliminado = Videojuego_Dao.eliminar(videojuego_1)
    log.debug(f"Videojuego eliminado: {videojuegos_eliminado}")

    #Seleccionar un registro
    videojuegos = Videojuego_Dao.seleccionar()
    for i in videojuegos:
        log.debug(i)