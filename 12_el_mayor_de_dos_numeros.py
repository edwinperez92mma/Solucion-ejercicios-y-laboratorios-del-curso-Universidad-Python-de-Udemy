print("El mayor de dos números - ejercicio")
"""
Solicitar al usuario dos valores y determinar cuál es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números (la salida debe ser idéntica a la que sigue):
Proporciona el número 1:
Proporciona el número 2:
El número mayor es: <numeroMayor>
"""

numero_1 = int(input("Digite el primer valor: "))
numero_2 = int(input("Digite el segundo valor: "))

if numero_1 > numero_2:
    print(f"El primer valor '{numero_1}' es el mayor")
elif numero_2 > numero_1:
    print(f"El segundo valor '{numero_2}' es el mayor")
else:
    print(f"Los valores '{numero_1}' y '{numero_2}' son iguales")
