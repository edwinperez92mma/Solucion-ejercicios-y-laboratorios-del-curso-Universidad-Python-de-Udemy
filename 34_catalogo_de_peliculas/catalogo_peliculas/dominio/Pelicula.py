class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

#Getter y setter para el atributo "nombre"
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

#Método __str__ para imprimir el estado del objeto
    def __str__(self):
        return f"{self.__nombre}"

#Pruebas de creación de objetos "Peliculas"
if __name__ == "__main__":
    pelicula_1 = Pelicula("The Matrix")
    pelicula_1.nombre = "Matrix"
    pelicula_2 = Pelicula("Spencer")
    pelicula_3 = Pelicula("The Northman")
    pelicula_4 = Pelicula("Licorice Pizza")
    pelicula_5 = Pelicula("Doctor Strange in the Multiverse of Madness")
    pelicula_5.nombre = "Doctor Strange en el multiverso de la locura"

    print(pelicula_1)
    print(pelicula_2)
    print(pelicula_3)
    print(pelicula_4)
    print(pelicula_5)