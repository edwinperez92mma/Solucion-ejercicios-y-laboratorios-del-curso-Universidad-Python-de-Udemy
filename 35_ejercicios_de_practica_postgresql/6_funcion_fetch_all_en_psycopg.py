print("Función fetch all en Psycopg")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM videojuegos WHERE id_videojuego IN %s"
            #llaves_primarias = ((1,2,3),)
            entrada = input("Proporciona los ID a buscar (separados por coma): ")
            llaves_primarias = (tuple(entrada.split(",")),)
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for i in registros:
                print(i)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()