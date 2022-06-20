print("Rectángulo - ejercicio propuesto")
#Instrucciones de la tarea:
"""
En el siguiente ejercicio se solicita calcular el área y el perímetro de un rectángulo, para ello debemos crear las siguientes variables:

alto (int)
ancho (int)

El usuario debe proporcionar los valores de largo y ancho, y después se debe imprimir el resultado en el siguiente formato (no usar acentos y
respetar los espacios, mayúsculas, minúsculas y saltos de línea):

Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perimetro: <perimetro>

Las fórmulas para calcular el área y el perímetro de un rectángulo son:
Area: alto * ancho
Perimetro: (alto + ancho) *2
"""

alto = int(input("Proporciona el alto: "))
ancho = int(input("Proporciona el ancho: "))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")