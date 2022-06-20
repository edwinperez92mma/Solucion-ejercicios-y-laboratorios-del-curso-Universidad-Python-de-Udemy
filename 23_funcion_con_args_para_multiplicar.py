print("Función con *args para multiplicar - ejercicio")
"""
Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y
regresar como resultado la multiplicación de todos los valores pasados como argumentos.
"""

def multiplicar(*args):
    numero = 1
    for i in args:
        numero *= i
    return numero

print(f"Resultado: {multiplicar(3,5,15,3)}")