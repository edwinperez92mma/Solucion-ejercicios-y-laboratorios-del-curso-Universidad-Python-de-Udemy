from Vehiculo import *

#Clase hija de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.__tipo = tipo
    
#Métodos set y get para tipo
    def set_tipo(self, tipo):
        self.__tipo = tipo

    """def get_tipo(self):#Esta no es necesaria porque tengo el método str pero igual la creo para practicar
        return self.__tipo"""

#Método str para recuperar información
    def __str__(self):
        return f"Tipo: {self.__tipo} - {super().__str__()}"