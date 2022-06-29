import os

class Catalogo_Peliculas:
    def __init__(self):
        self.__ruta = "archivo.txt"

#Getter y setter para el atributo "ruta"
    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, ruta):
        self.__ruta = ruta

    def agregar_peliculas(self, pelicula):
        with open(self.ruta, "a", encoding="utf8") as archivo:
            archivo.write(f"{pelicula.nombre}\n")

    def listar_peliculas(self):
        with open(self.ruta, "r", encoding="utf8") as archivo:
            print("")
            print("Catálogo películas".center(50, "*"))
            print(archivo.read())

    def eliminar_archivo(self):
        os.remove(self.ruta)
        print(f"Archivo eliminado: {self.ruta}")