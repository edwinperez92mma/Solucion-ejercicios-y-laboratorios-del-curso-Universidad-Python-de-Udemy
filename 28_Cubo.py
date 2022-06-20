"""
class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    
    def calcular_volumen(self):
        ancho = float(input("Proporciona el ancho: "))
        alto = float(input("Proporciona el alto: "))
        profundo = float(input("Proporciona la profundida: "))
        print(f"Volumen del cubo: {ancho * alto * profundo}")

cubo_1 = Cubo(None, None, None)
cubo_1.calcular_volumen()
"""

print("Solución propuesta por el instructor")

class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo


ancho = int(input("Proporciona el ancho: "))
alto = int(input("Proporciona el alto: "))
profundo = int(input("Proporciona el profundo: "))

cubo_1 = Cubo(ancho, alto, profundo)

print(f"Volumen del cubo: {ancho * alto * profundo}")