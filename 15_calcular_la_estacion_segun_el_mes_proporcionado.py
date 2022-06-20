print("Calcular la estación según el mes proporcionado - ejercicio")
#Se le pedirá al usuario que introduzca el mes del año (valor entre 1 y 12), y según el valor devolveremos un mensaje con el nombre de la estación
#correspondiente al mes proporcionado

mes = int(input("Digite el mes actual (números de 1 a 12): "))

estacion = None

def numeros_a_texto(num):
    if num == 12 or num == 1 or num == 2:
        num = "Invierno"
    elif num == 3 or num == 4 or num == 5:
        num = "Primavera"
    elif num == 6 or num == 7 or num == 8:
        num = "Verano"
    elif num == 9 or num == 10 or num == 11:
        num = "Otoño"
    else:
        num = "Mes incorrecto"
    return num

print(f"Para el mes {mes} la estación es: {numeros_a_texto(mes)}")