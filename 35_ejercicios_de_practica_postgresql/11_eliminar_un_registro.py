print("Eliminar un registro")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM videojuegos WHERE id_videojuego=%s"
            entrada = input("Digita el id_videojuego a eliminar: ")
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()