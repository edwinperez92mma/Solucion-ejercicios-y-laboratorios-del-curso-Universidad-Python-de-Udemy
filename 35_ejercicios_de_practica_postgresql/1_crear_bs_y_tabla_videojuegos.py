print("Creación de la base de datos y la tabla persona")

#1.La base de datos será creada mediante Postgresql. Se trata de un pequeño catalogo con datos sobre mis videojuegos favoritos:
"""
Nombre de la base de datos: ejercicio_postgresql

Nombre de la tabla: videojuegos
Owner: postgres
Schema: public

Columnas:

1ra columna
Name: id_videojuego
Data type: serial
Not Null?: Yes
Primary Key?: Yes

2da columna
Name: nombre
Data type: character varying
Not Null?: No
Primary Key?: No

3ra columna
Name: genero
Data type: character varying
Not Null?: No
Primary Key?: No

4ta columna
Name: desarrolladora
Data type: character varying
Not Null?: No
Primary Key?: No

5ta columna
Name: plataforma
Data type: character varying
Not Null?: No
Primary Key?: No

6ta año
Name: año
Data type: integer
Not Null?: No
Primary Key?: No
"""

#Agregamos 2 registros directamente por pgAdmin:
"""
1er registro
Nombre: Resident Evil 3: Nemesis
Genero: Terror
Desarrolladora: Capcom
Plataforma: PlayStation
Año: 1999

2do registro
Nombre: Grand Theft Auto: Vice City
Genero: Sandbox
Desarrolladora: Rockstar Games
Plataforma: PlayStation 2
Año: 2002
"""