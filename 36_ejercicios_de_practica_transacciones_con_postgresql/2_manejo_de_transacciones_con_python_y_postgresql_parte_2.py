print("Manejo de Transacciones con Python y Postgresql parte 2")

import psycopg2 as bd

conexion = bd.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    conexion.autocommit = False

    cursor = conexion.cursor()
    sentencia = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
    valores = ("Perfect Dark", "FPS", "Rare", "Nintendo 64", 2000)
    cursor.execute(sentencia, valores)

    sentencia = "UPDATE videojuegos SET nombre=%s, genero=%s, desarrolladora=%s, plataforma=%s, año=%s WHERE id_videojuego=%s"
    valores = ("Resident Evil", "Survival Horror", "Capcom", "Play Station", 1992, 1)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print("Termina la transacción, se hizo commit")
except Exception as e:
    conexion.rollback()
    print(f"Ocurrió un error, se hizo rollback: {e}")
finally:
    conexion.close()