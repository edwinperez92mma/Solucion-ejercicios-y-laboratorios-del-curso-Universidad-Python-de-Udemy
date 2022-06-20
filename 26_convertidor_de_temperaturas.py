print("Convertidor de temperaturas")
"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
"""

"""
opcion = int(input("Presione 1 para convertir de grados celsius a fahrenheit\nO presione 2 para convertir de grados fahrenheit a celsius: "))

def celsius_a_fahrenheit():
        celsius = float(input("Grados celsius: "))
        fahrenheit = (celsius*1.8)+32
        print(f"{celsius} grados celsius equivalen a {fahrenheit} grados fahrenheit: ")

def fahrenheit_a_celsius():
        fahrenheit = float(input("Grados fahrenheit: "))
        celsius = (fahrenheit-32)*0.5556
        print(f"{fahrenheit} grados fahrenheit equivalen a {celsius} grados celsius: ")

def conversion(opc):
    if opc == 1:
        celsius_a_fahrenheit()
    elif opc == 2:
        fahrenheit_a_celsius()
    else:
        print("Opcion incorrecta")

conversion(opcion)
"""

print("Solución propuesta por el instructor")

#Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius*9/5+32

#Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

#Realizamos pruebas de conversión
celsius = float(input("Proporcione su valor en celsius: "))
resultado = celsius_fahrenheit(celsius)
#Imprimimos el resultado
print(f"{celsius} C a F: {resultado:.2f}")#El :.2f es para que solo imprima 2 valores flotantes

#Realizamos la prueba de grados fahrenheit a celsius
fahrenheit = float(input("Proporcione su valor en fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
#imprimimos el resultado
print(f"{fahrenheit} F a C: {resultado:.2f}")