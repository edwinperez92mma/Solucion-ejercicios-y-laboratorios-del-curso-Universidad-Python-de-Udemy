print("Valor dentro de rango - ejercicio")
#Vamos a pedirle al usuario que ingrese un valor, y debemos verificar si dicho valor se encuentra dentro del rango de 0 a 5

valor = int(input("Valor: "))

if valor >= 0 and valor <= 5:
    print(f"El valor '{valor}' SÍ se encuentra dentro del rango de 0 a 5")
else:
    print(f"El valor '{valor}' NO se encuentra dentro del rango de 0 a 5")