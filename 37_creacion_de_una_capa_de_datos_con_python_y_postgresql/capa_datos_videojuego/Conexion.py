from logger_base import log
import psycopg2 as bd
import sys

class Conexion:
    def __init__(self):
        self.__DATABASE = ""
        self.__USERNAME = "postgres"
        self.__PASSWORD = "admin"
        self.__DB_PORT = "5432"
        self.__HOST = "127.0.0.1"
        self.__DATABASE = "ejercicio_postgresql"
        self.__conexion = None
        self.__cursor = None
    
    def obtener_conexion(self):
        if self.__conexion == None:
            try:
                self.__conexion = bd.connect(host=self.__HOST,
                                            user=self.__USERNAME,
                                            password=self.__PASSWORD,
                                            port=self.__DB_PORT,
                                            database=self.__DATABASE
                                            )
                log.debug(f"Conexión exitosa: {self.__conexion}")
                return self.__conexion
            except Exception as e:
                log.error(f"Ocurrió una excepción al obtener la conexión: {e}")
                sys.exit()
        else:
            return self.__conexion

    def obtener_cursor(self):
        if self.__cursor == None:
            try:
                cursor = self.__cursor
                self.__cursor = self.obtener_conexion().cursor()
                log.debug(f"Se abrió correctamente el cursor: {self.__cursor}")
                return self.__cursor
            except Exception as e:
                log.error(f"Ocurrió una excepción al obtener el cursor: {e}")
                sys.exit()
        else:
            return self.__cursor

if __name__ == "__main__":
    conexion_1 = Conexion()
    conexion_1.obtener_conexion()
    conexion_1.obtener_cursor()