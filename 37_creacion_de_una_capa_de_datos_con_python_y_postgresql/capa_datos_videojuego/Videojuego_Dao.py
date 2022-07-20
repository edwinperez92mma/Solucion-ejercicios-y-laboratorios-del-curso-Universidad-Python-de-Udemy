from logger_base import log
from Videojuego import Videojuego
from Conexion import Conexion

class Videojuego_Dao:
    def __init__(self):
        self.__SELECCIONAR = "SELECT * FROM videojuegos ORDER BY id_videojuego ASC"
        self.__INSERTAR = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
        self.__ACTUALIZAR = "UPDATE videojuegos SET nombre=%s, genero=%s, desarrolladora=%s, plataforma=%s, año=%s WHERE id_videojuego=%s"
        self.__ELIMINAR = "DELETE FROM videojuegos WHERE id_videojuego=%s"

    def seleccionar(self):
        conexion = Conexion()
        with conexion.obtener_conexion():
            with conexion.obtener_cursor() as cursor:
                cursor.execute(self.__SELECCIONAR)
                registros = cursor.fetchall()
                videojuegos = []
                for i in registros:
                    videojuego = Videojuego(i[0], i[1], i[2], i[3], i[4], i[5])
                    videojuegos.append(videojuego)
            return videojuegos
    
    def insertar(self, videojuego):
        conexion = Conexion()
        with conexion.obtener_conexion():
            with conexion.obtener_cursor() as cursor:
                valores = (videojuego.nombre, videojuego.genero, videojuego.desarrolladora, videojuego.plataforma, videojuego.año)
                cursor.execute(self.__INSERTAR, valores)
                log.debug(f"Videojuego insertado: {videojuego}")
                return cursor.rowcount

    def actualizar(self, videojuego):
        conexion = Conexion()
        with conexion.obtener_conexion():
            with conexion.obtener_cursor() as cursor:
                valores = (videojuego.nombre, videojuego.genero, videojuego.desarrolladora, videojuego.plataforma, videojuego.año, videojuego.id_videojuego)
                cursor.execute(self.__ACTUALIZAR, valores)
                log.debug(f"Videojuego actualizado: {videojuego}")
                return cursor.rowcount

    def eliminar(self, videojuego):
        conexion = Conexion()
        with conexion.obtener_conexion():
            with conexion.obtener_cursor() as cursor:
                valores = (videojuego.id_videojuego,)
                cursor.execute(self.__ELIMINAR, valores)
                log.debug(f"Videojuego eliminado: {videojuego}")
                return cursor.rowcount

if __name__ == "__main__":
    #Insertar un registro
    #videojuego_1 = Videojuego(nombre="Super Mario 64", genero="Aventura", desarrolladora="Nintendo", plataforma="Nintendo 64", año=1996)
    #videojuegos_insertados = Videojuego_Dao().insertar(videojuego_1)
    #log.debug(f"Videojuegos insertados: {videojuegos_insertados}")

    #Actualizar un registro
    #videojuego_1 = Videojuego(1, "Resident Evil 1", "Survival Horror", "Capcom", "Play Station", 1996)
    #videojuego_actualizado = Videojuego_Dao().actualizar(videojuego_1)
    #log.debug(f"Videojuego actualizado: {videojuego_actualizado}")

    #Eliminar un registro
    videojuego_1 = Videojuego(id_videojuego=13)
    videojuego_eliminado = Videojuego_Dao().eliminar(videojuego_1)
    log.debug(f"Videojuego eliminado: {videojuego_1}")

    #Seleccionar un registro
    videojuego = Videojuego_Dao().seleccionar()
    for i in videojuego:
        log.debug(i)