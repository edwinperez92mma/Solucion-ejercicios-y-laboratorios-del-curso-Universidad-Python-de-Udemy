print("Rango entre 20's y 30's - ejercicio")
#Combinaremos los operadores and y or para saber si la edad de una persona se encuentra entre los 20 y los 30

edad = int(input("Digite su edad: "))

veintes = edad >= 20 and edad < 30
treintas = edad >= 30 and edad < 40

print(f"Veintes: {veintes}")
print(f"Treintas: {treintas}")

if veintes or treintas:
    if veintes:
        print("Dentro de los 20's")
    elif treintas:
        print("Dentro de los 30's")
    else:
        print("Fuera de rango")
else:
    print("No está dentro de los 20's y 30'")

#Otra manera
"""if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print("Dentro de rango 20's y 30's")
else:
    print("No está dentro de los 20's y 30'")"""