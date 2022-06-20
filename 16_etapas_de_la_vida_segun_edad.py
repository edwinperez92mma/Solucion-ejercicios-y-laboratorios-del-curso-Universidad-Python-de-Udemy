print("Etapas de la vida según edad - ejercicio")
"""
Proporciona tu edad

0-10: La infancia es increíble...
10-20: Muchos cambios y mucho estudio...
20-30: Amor y comienza el trabajo...

Cualquier otro valor: Etapa no reconocida
"""

"""edad = int(input("Proporciona tu edad: "))

def evaluar_edad(dato):
    if dato == 1 or dato == 2 or dato == 3 or dato == 4 or dato == 5 or dato == 6 or dato == 7 or dato == 8 or dato == 9 or dato == 10:
        print(f"Edad: {edad} - La infancia es increíble...")
    elif dato == 11 or dato == 12 or dato == 13 or dato == 14 or dato == 15 or dato == 16 or dato == 17 or dato == 18 or dato == 19 or dato == 20:
        print(f"Edad: {edad} - Muchos cambios y mucho estudio...")
    elif dato == 21 or dato == 22 or dato == 23 or dato == 24 or dato == 25 or dato == 26 or dato == 27 or dato == 28 or dato == 29 or dato == 30:
        print(f"Edad: {edad} - Amor y comienza el trabajo...")
    else:
        print("Etapa no reconocida")

evaluar_edad(edad)"""

"""print("Solución propuesta por el instructor")

edad = int(input("Proporciona tu edad: "))

def evaluar_edad(dato):
    if dato >= 0 and dato < 10:
        print(f"Edad: {edad} - La infancia es increíble...")
    elif dato >= 10 and dato < 20:
        print(f"Edad: {edad} - Muchos cambios y mucho estudio...")
    elif dato >= 20 and dato < 30:
        print(f"Edad: {edad} - Amor y comienza el trabajo...")
    else:
        print("Etapa no reconocida")

evaluar_edad(edad)"""

print("Solución con operador ternario")

edad = int(input("Proporciona tu edad: "))

def evaluar_edad(dato):
    if 0 <= dato < 10:
        print(f"Edad: {edad} - La infancia es increíble...")
    elif 10 <= dato < 20:
        print(f"Edad: {edad} - Muchos cambios y mucho estudio...")
    elif 20 <= dato < 30:
        print(f"Edad: {edad} - Amor y comienza el trabajo...")
    else:
        print("Etapa no reconocida")

evaluar_edad(edad)