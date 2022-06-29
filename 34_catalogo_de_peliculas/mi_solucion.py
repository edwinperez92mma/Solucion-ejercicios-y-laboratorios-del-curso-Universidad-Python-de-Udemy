print("Laboratorio final")
#Ver imagen "catalogo_uml.jpg" para información sobre las clases y sus relaciones.

#1.Los archivos se encontrará en una carpeta principal llamada "catalogo_peliculas".

#2.La clase "Pelicula" va a estar contenida dentro del paquete (carpeta o folder) "dominio".

#3.La clase "CatalogoPeliculas" va a estar contenida dentro del paquete "servicio".

#4.Crearemos un archivo de pruebas llamado "test_catalogo_peliculas.py".

#Explicación clases:

#Clase 1 (dentro de la carpeta "dominio"):
"""
Nombre:
Pelicula

Atributos:
- nombre: str

Métodos:
+ __str__()

Responsabilidades:
-- Representa un objeto película
"""

#Clase 2 (dentro de la carpeta "servicio"):
"""
Nombre:
CatalogoPeliculas

Atributos:
+ ruta_archivo: str <<static>> (va a ser el nombre del archivo de texto con el que vamos a trabajar, por ejemplo "peliculas.txt")

Métodos:
+ agregar_pelicula(Pelicula) <<static>> (recibe un objeto de tipo "Pelicula". Se recomienda que esté en modo "append" para agregar más películas)
+ listar_peliculas() <<static>> (lista los nombres de las películas de nuestro archivo)
+ eliminar() <<static>> (para pode eliminar un archivo, tenemos que importar el paquete "os", y para implementarlo usamos el método
"os.remove("peliculas.txt")", y como parámetro va la ruta (path) del archivo que vamos a eliminar)


Responsabilidades:
-- Representa un objeto película
"""

#Archivo de pruebas:
"""
Nombre:
"test_catalogo_peliculas.py"

Responsabilidades:
-- Contiene un menú con 4 opciones:
    1)Agregar película
    2)Listar películas
    3)Eliminar archivo de películas
    4)Salir
"""
#En consola se deben mostrar las opciones así:
"""
Opciones:
1. Agregar película
2. Listar películas
3. Eliminar catágolo de películas
4. Salir
"""
#Si presionamos 1, nos pregunta:
"""
Proporciona la película: Batman
"""