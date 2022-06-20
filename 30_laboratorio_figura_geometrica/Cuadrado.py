from Figura_Geometrica import Figura_Geometrica
from Color import Color

class Cuadrado(Figura_Geometrica, Color):
    def __init__(self, lado, color):
        Figura_Geometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

#Método para calcular el área de un cuadrado (lado * lado)
    def calcular_area(self):
        return self.get_ancho() * self.get_alto()

#Método str para imprimir información
    def __str__(self):
        return f"{super().__str__()} - Color: {self.get_color()} - Área Cuadrado: {self.calcular_area()}"

#print(Cuadrado.mro())

"""cuadrado_1 = Cuadrado(5, "rojo")
print(cuadrado_1)"""