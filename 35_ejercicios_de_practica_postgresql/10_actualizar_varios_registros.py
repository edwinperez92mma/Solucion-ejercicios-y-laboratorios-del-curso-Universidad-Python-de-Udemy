print("Actualizar varios registros")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE videojuegos SET nombre=%s, genero=%s, desarrolladora=%s, plataforma=%s, año=%s WHERE id_videojuego=%s"
            valores = (
                ("Sonic Adventure 1", "Aventura", "Sonic Team", "Sega Dreamcast", 1998, 7),
                ("Warcraft III: Reign of Chaos", "Estrategia ", "Blizzard Entertainment", "Microsoft Windows", 2002, 5),
                ("Grand Theft Auto III", "Acción-Aventura", "Rockstar", "Play Station 2", 2001, 2)
                )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros actualizados: {registros_actualizados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()