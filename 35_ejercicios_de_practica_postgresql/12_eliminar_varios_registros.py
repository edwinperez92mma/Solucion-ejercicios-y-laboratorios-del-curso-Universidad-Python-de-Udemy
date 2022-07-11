print("Eliminar varios registros")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM videojuegos WHERE id_videojuego IN %s"
            entrada = input("Digita los id_videojuego a eliminar (separados por coma): ")
            valores = (tuple(entrada.split(",")),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()