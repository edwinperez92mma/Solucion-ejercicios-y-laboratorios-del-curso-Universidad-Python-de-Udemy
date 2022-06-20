print("Sistema de calificaciones - ejercicio")
"""
Instrucciones de la tarea:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
Caulquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
Proporciona un valor entre 0 y 10:
A
"""

"""calificacion = float(input("Proporciona una calificación entre 0 y 10: "))

def evaluacion(dato):
    if dato >= 9 and dato <=10:
        print(f"Nota {dato}: A")
    elif dato >= 8 and dato <9:
        print(f"Nota {dato}: B")
    elif dato >= 7 and dato <8:
        print(f"Nota {dato}: C")
    elif dato >= 6 and dato <7:
        print(f"Nota {dato}: D")
    elif dato >= 0 and dato <6:
        print(f"Nota {dato}: D")
    else:
        print(f"{dato}: valor incorrecto")

evaluacion(calificacion)"""

print("Solución con valor ternario")

calificacion = float(input("Proporciona una calificación entre 0 y 10: "))

def evaluacion(dato):
    if 9 <= dato <=10:
        print(f"Nota {dato}: A")
    elif 8 <= dato <9:
        print(f"Nota {dato}: B")
    elif 7 <= dato <8:
        print(f"Nota {dato}: C")
    elif 6 <= dato <7:
        print(f"Nota {dato}: D")
    elif 0 <= dato <6:
        print(f"Nota {dato}: D")
    else:
        print(f"{dato}: valor incorrecto")

evaluacion(calificacion)