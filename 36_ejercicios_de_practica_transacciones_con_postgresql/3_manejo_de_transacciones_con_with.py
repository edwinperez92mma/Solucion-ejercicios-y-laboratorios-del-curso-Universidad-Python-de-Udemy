print("Manejo de Transacciones con with")

import psycopg2 as bd

conexion = bd.connect(user = "postgres", password = "admin", host = "127.0.0.1", port = "5432", database = "ejercicio_postgresql")

try:
    with conexion:
        with conexion.cursor() as cursor:
            
            sentencia = "INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES(%s, %s, %s, %s, %s)"
            valores = ("Super Mario World 2: Yoshi's Island", "Plataformas", "Nintendo", "Super Nintendo", 1995)
            cursor.execute(sentencia, valores)

            sentencia = "UPDATE videojuegos SET nombre=%s, genero=%s, desarrolladora=%s, plataforma=%s, año=%s WHERE id_videojuego=%s"
            valores = ("Resident Evil 3", "Survival Horror", "Capcom", "Play Station", 1999, 1)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f"Ocurrió un error, se hizo rollback: {e}")
finally:
    conexion.close()

print("Termina la transacción, se hizo commit")