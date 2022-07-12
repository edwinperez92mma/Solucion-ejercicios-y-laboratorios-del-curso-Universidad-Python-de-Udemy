print("Ejercicios de práctica Transacciones con Postgresql")

import psycopg2 as bd

conexion = bd.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
    valores = ("Warcraft II: Tides of Darkness", "Estrategia", "Blizzard Entertainment", "Microsoft Windows", 1995)
    cursor.execute(sentencia, valores)
    conexion.commit()
    print("Termina la transacción")
except Exception as e:
    conexion.rollback()
    print(f"Ocurrió un error, se hizo rollback: {e}")
finally:
    conexion.close()