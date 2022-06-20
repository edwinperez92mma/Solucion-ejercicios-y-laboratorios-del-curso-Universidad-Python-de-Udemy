from Figura_Geometrica import Figura_Geometrica
from Color import Color
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Objeto 1 - Clase Figura")
figura_1 = Figura_Geometrica(5, 5)
print(figura_1)
print(Figura_Geometrica.mro())

print("\nObjeto 2 - Clase Color")
color_1 = Color("rojo")
print(f"Color: {color_1.get_color()}")
print(Color.mro())

print("\nObjeto 3 - Clase Cuadrado")
cuadrado_1 = Cuadrado(5, "azul")
print(cuadrado_1)
print(Cuadrado.mro())

print("\nObjeto 4 - Clase Rectángulo")
rectangulo_1 = Rectangulo(5, 10, "verde")
print(rectangulo_1)
print(Rectangulo.mro())