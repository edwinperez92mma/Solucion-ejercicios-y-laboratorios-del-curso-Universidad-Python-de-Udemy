from dominio.Pelicula import Pelicula
from servicio.Catalogo_Peliculas import Catalogo_Peliculas

opcion = None
catalogo = Catalogo_Peliculas()

while opcion != 4:
    try:
        opcion = int(input("\nOpciones:\n1.Agregar película\n2.Listar películas\n3.Eliminar catalogo:\n4.Salir\nDigite la opción deseada (1-4): " ))

        if opcion == 1:
            nombre = input("Digite el nombre de la película: ")
            pelicula = Pelicula(nombre)
            catalogo.agregar_peliculas(pelicula)
        elif opcion == 2:
            catalogo.listar_peliculas()
        elif opcion == 3:
            catalogo.eliminar_archivo()

    except Exception as e:
        print(f"\nError: {e}")
        opcion = None
else:
    print("Ha salido del programa")