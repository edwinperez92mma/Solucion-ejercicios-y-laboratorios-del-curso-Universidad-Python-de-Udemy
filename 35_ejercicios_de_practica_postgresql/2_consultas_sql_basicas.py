print("Consultas SQL Básicas")

#1.En el editor de queries de pgAdmin de nuestra tabla "videojuegos", con el siguiente código:
"""
SELECT * FROM videojuegos
"""
#Al ejecutarlo nos mostrarán la tabla "videojuegos" con sus columnas y registros.

#2.Para limitar la cantidad de información de tablas y columnas que queremos ver, podemos añadir este filtro:
"""
SELECT * FROM videojuegos WHERE id_videojuego=1
"""
#Allí estamos específicando que nos muestre el primer registro de la llave primaria "id_videojuego".

#3.Pero si queremos más de un registro, también podemos especificarlo entre paréntesis:
"""
SELECT * FROM videojuegos WHERE id_videojuego in (1,2)
"""
#Nota: si proporcionamos un valor no existente, como el 3, igual solo se nos mostrará la información existente.

#4.Comentamos la instrucción con doble guión "--" para que ya no se ejecute:
"""
--SELECT * FROM videojuegos WHERE id_videojuego in (1,2)
"""

#5.Para insertar información con código SQL, usamos la sentencia INSERT INTO para especificar la tabla en la que agregaremos información. Entre
#paréntesis indicamos las columnas que vamos a afectar (la columna de id_persona no la especificamos porque esa es automática). Luego usamos la
#palabra VALUES para especificar los valores que vamos a pasar:
"""
INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES('Age of Empires II: The Age of Kings', 'Estrategia en tiempo real', 'Ensemble Studios', 'Microsoft Windows', 1999)
"""
#Nota: los valores que vamos a pasar deben estar entre comillas simples '.
#Al ejecutar la consola nos confirma el éxito del la inserción del registro. Pero debemos comentar el código de la inserción y ejecutar otra vez el
#primer código para ver nuestra tabla, ya que si no comentamos la línea de inserción, se volverán a insertar esos valores:
"""
--SELECT * FROM videojuegos WHERE id_videojuego in (1,2)
--INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES('Age of Empires II: The Age of Kings', 'Estrategia en tiempo real', 'Ensemble Studios', 'Microsoft Windows', 1999)
SELECT * FROM videojuego
"""
#Ahora se nos muestra la tabla con 3 registros.

#6.Para modificar un valor ya existente usamos la sentencia UPDATE. Luego especificamos la tabla, y con SET especificamos qué valores queremos
#afectar ya que no es obligatorio modificar todas las columnas de un registro. Por ejemplo, si queremos modificar el nombre del registro 3,
#digitamos:
"""
--SELECT * FROM videojuegos WHERE id_videojuego in (1,2)
--INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES('Age of Empires II: The Age of Kings', 'Estrategia en tiempo real', 'Ensemble Studios', 'Microsoft Windows', 1999)
--SELECT * FROM videojuego
UPDATE videojuegos SET genero='Survival horror' WHERE id_videojuego=1
"""
#Nota: es importante usar la palabra WHERE para especificar en qué registro hay que hacer los cambios, ya que si no usamos WHERE, la nueva infomración
#será añadida en todos los registros arruinando nuestra base de datos.
#Nota 2: después de ejecutar no olvidar comentar esa línea y volver a usar un SELECT * FROM para volver a ver nuestra tabla.

#7.Para eliminar un registro, usamos las palabras DELETE FROM seguidas de la tabla de la que vamos a borrar información. Luego va el filtro WHERE
#seguido del id. Si no usamos el WHERE, se borrarán todos los registros:
"""
--SELECT * FROM videojuegos WHERE id_videojuego in (1,2)
--INSERT INTO videojuegos(nombre, genero, desarrolladora, plataforma, año) VALUES('Age of Empires II: The Age of Kings', 'Estrategia en tiempo real', 'Ensemble Studios', 'Microsoft Windows', 1999)
--SELECT * FROM videojuego
--UPDATE videojuegos SET genero='Survival horror' WHERE id_videojuego=1
DELETE FROM videojuegos WHERE id_videojuego=3
"""
#Nota: si quisieramos borrar vários registros, se hace prácticamente igual a cuando vamos a insertar registros:
#DELETE FROM persona WHERE id_persona IN (3,2,1)
#Pero en este ejercicio solo vamos a eliminar el registro 3