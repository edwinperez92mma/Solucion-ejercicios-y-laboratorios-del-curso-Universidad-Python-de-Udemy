print("Uso de rangos - ejercicio")
#Sintáxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

#Ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
"""
Resultado esperado en consola:
0
3
6
9
"""

#Ejercicio 2. Crear un rango de números de 2 a 6 e imprimirlos
"""
Resultado esperado en consola:
2
3
4
5
6
"""

#Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1
"""
Resultado esperado en consola:
3
5
7
9
"""

"""print("\nEjericio 1")

for i in range(0,10):
    if i % 3 == 0:
        print(i)
        i += 1

print("\nEjericio 2")

for j in range(2,7,+1):
    print(j)

print("\nEjericio 3")

for k in range(3,11,+2):
    print(k)"""

print("Soluciones propuestas por el instructor")

print("\nEjericio 1")

for i in range(11):
    if i % 3 == 0:
        print(i)

print("\nEjericio 2")

rango = range(2,7)

for j in rango:
    print(j)

print("\nEjericio 3")

rango = range(3,11,2)

for k in rango:
    print(k)