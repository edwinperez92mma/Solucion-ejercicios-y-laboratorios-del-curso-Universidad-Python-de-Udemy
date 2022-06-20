print("Conversión de números a texto - ejercicio")
#Proporcionar un valor entre 1 y 3 y convertirlo a texto

numero = int(input("Digita un número de 1 a 3: "))

def convertir_a_texto(num):
    if num == 1:
        num = "Uno"
    elif num == 2:
        num = "Dos"
    elif num == 3:
        num = "Tres"
    else:
        num = "Valor fuera del rango de 1 a 3"
    return num

print(f"Número proporcionado: {numero} - '{convertir_a_texto(numero)}'")