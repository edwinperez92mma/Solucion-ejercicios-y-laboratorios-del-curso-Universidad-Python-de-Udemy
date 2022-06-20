from Figura_Geometrica import Figura_Geometrica
from Color import Color

class Rectangulo(Figura_Geometrica, Color):
    def __init__(self, alto, ancho, color):
        Figura_Geometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

#Método para calcular el área de un rectángulo (alto * ancho)
    def calcular_area(self):
        return self.get_alto() * self.get_ancho()

#Método str para imprimir información
    def __str__(self):
        return f"{super().__str__()} - Color: {self.get_color()} - Área rectángulo: {self.calcular_area()}"

#print(Rectangulo.mro())

"""rectangulo_1 = Rectangulo(5, 10, "verde")
print(rectangulo_1)"""