print("Uso de tuplas y listas - ejercicio")
#Dada la siguiente tupla, crear una lista que solo incluya los números menores a 5:
#tupla = (13, 1, 8, 3, 2, 5, 8)
#El resultado final es una lista que imprime esto: [1, 3, 2]

"""
tupla = (13, 1, 8, 3, 2, 5, 8)

lista = list(tupla)

lista_2 = []

for i in lista:
    if i < 5:
        lista_2.append(i)

print(lista_2)
"""

print("Solución propuesta por el instructor")

tupla = (13, 1, 8, 3, 2, 5, 8)

#Definir la lista
lista = []

#Filtramos los elementos menores a 5 de la tupla
for i in tupla:
    if i < 5:
        lista.append(i)

#Imprimimos la lista
print(lista)