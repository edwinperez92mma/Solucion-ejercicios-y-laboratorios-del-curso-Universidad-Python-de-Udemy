print("Insertar varios registros")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
            valores = (
                ("Warcraft II: Tides of Darkness", "Estrategia", "Blizzard Entertainment", "Microsoft Windows", 1995),
                ("Perfect Dark", "Disparos en primera persona", "Rare", "Nintendo 64", 2000),
                ("Sonic Adventure", "Aventura", "Sonic Team", "Sega Dreamcast", 1998)
            )
            cursor.executemany(sentencia, valores)
            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()