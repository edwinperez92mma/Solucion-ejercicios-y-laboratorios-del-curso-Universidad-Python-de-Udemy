from Vehiculo import *

#Clase hija de Vehiculo
class Coche(Vehiculo):
    def __init__(self, color, ruedas, kilometros):
        super().__init__(color, ruedas)
        self.__kilometros = kilometros

#Métodos set y get para kilometros
    def set_kilometros(self, kilometros):
        self.__kilometros = kilometros

    """def get_kilometros(self):#Esta no es necesaria porque tengo el método str pero igual la creo para practicar
        return self.__kilometros"""

#Método str para recuperar información
    def __str__(self):
        return f"Kilómetros: {self.__kilometros} - {super().__str__()}"