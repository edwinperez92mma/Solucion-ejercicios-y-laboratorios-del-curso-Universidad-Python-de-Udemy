print("Función fetch one en Psycopg")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM videojuegos WHERE id_videojuego=%s"
            id_videojuego = input("Proporciona el valor de id_videojuego: ")
            cursor.execute(sentencia, (id_videojuego,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()