print("Actualizar un registro")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE videojuegos SET nombre=%s, genero=%s, desarrolladora=%s, plataforma=%s, año=%s WHERE id_videojuego=%s"
            valores = ("Sonic Adventure 2", "Aventura", "Sonic Team", "Sega Dreamcast", 2001, 7)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros actualizados: {registros_actualizados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()