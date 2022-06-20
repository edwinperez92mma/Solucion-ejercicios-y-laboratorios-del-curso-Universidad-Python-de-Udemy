print("Tienda de libros - ejercicio")
#Solicitamos al usuario el nombre del libro
#Proporcionar el ID del libro (número entero)
#Proporcionar el precio (valor flotante)
#Indicar si el envío es gratuito escribiendo True or False
#Luego se imprimen los datos suministrados por el usuario: Nombre: - ID: - Precio: - ¿Envío gratuito?:

nombre = input("Nombre del libro: ")
id = int(input("ID del libro: "))
valor = float(input("Precio: "))
envio = input("¿El envío es gratuito? (True or False): ")
#No se puede usar bool() porque lo que siempre hace es retornar True en caso de detectar una cadena

def invertir_boolean(dato):#Hice esta función porque al convertir el string a boolean en la línea anterior, la consola imprimía el valor opuesto
    global envio
    if dato == "True":
        envio = True
    elif dato == "False":
        envio = False
    return envio

envio_boolean = invertir_boolean(envio)

print(f"Nombre: {nombre}\nID: {id}\nPrecio: {valor}\n¿Envío gratuito?: {envio_boolean}")

print(type(envio_boolean))#Esto solo es para verificar que el valor de la variable sea bool