"""
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        print(f"Área rectángulo: {self.base * self.altura}")

base = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))

rectangulo_1 = Rectangulo(base, altura)
rectangulo_1.calcular_area()
"""

print("Solución propuesta por el instructor")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))

rectangulo_1 = Rectangulo(base, altura)
print(f"Área rectángulo: {rectangulo_1.calcular_area()}")

base = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))

rectangulo_2 = Rectangulo(base, altura)
print(f"Área rectángulo: {rectangulo_2.calcular_area()}")