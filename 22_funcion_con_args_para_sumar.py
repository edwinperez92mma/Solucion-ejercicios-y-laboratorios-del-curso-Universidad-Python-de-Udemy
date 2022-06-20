print("Función con *args para sumar - ejercicio")
"""
Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función, y regresar
como resultado la suma de todos los valores pasados como argumentos
"""

def sumar(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

numeros = sumar(3, 5, 9, 4, 6)
print(numeros)