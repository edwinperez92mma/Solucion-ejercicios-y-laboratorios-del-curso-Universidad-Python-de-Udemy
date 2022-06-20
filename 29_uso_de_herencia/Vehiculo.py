#Clase Padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self.__color = color
        self.__ruedas = ruedas

#Métodos set y get para color
    def set_color(self, color):
        self.__color = color

    """def get_color(self):#Esta no es necesaria porque tengo el método str pero igual la creo para practicar
        return self.__color"""

#Métodos set y get para ruedas
    def set_ruedas(self, ruedas):
        self.__ruedas = ruedas

    """def get_ruedas(self):#Esta no es necesaria porque tengo el método str pero igual la creo para practicar
        return self.__ruedas"""

#Método str para recuperar información
    def __str__(self):
        return f"Color: {self.__color} - Ruedas: {self.__ruedas}"