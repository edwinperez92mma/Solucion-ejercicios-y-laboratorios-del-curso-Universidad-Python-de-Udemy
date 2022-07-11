print("Insertar registro con Psycopg")

import psycopg2

conexion = psycopg2.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
            valores = ("Age of Empires II: The Age of Kings", "Estrategia", "Ensemble Studios", "Microsoft Windows", 1999)
            cursor.execute(sentencia, valores)
            #conexion.commit()
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    conexion.close()