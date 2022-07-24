from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = "ejercicio_postgresql"
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                        host=cls._HOST,
                                                        user=cls._USERNAME,
                                                        password=cls._PASSWORD,
                                                        port=cls._DB_PORT,
                                                        database=cls._DATABASE)
                log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrió un error al obtener el pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"Regresamos la conexión al pool: {conexion}")

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
    
if __name__ == "__main__":
    conexion_1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_1)

    conexion_2 = Conexion.obtenerConexion()

    conexion_3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_3)
    
    conexion_4 = Conexion.obtenerConexion()

    conexion_5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion_5)

    conexion_6 = Conexion.obtenerConexion()