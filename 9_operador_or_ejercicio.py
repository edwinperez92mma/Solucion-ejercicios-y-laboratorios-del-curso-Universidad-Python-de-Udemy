print("Operador or - ejercicio")
#Escribir un programa para saber si un padre puede o no asistir al juego de su hijo
#Si está de vacaciones o si está en un día de descanso, sí puede asistir al juego, de lo contrario no podrá

#Le solicitamos las entradas al usuario
vacaciones = input("¿Está de vacaciones? (si o no): ")
descanso = input("¿Es su día de descanso? (si o no): ")

#Aquí se convierten las entradas del usuario a minúsculas
vacaciones_minuscula = vacaciones.lower()
descanso_minuscula = descanso.lower()

#Con esta función eliminamos los posibles acentos que el usuario digite
def eliminar_tildes(palabra):
    for i in palabra:
        if palabra == "sí" or palabra == "sì" or palabra == "sî":
            palabra = "si"
        elif palabra == "nó" or palabra == "nò" or palabra == "nô":
            palabra = "no"
    return palabra

#Aquí llamamos a la anterior función para eliminar los acentos
vacaciones_minuscula = eliminar_tildes(vacaciones_minuscula)
descanso_minuscula = eliminar_tildes(descanso_minuscula)

#Esto solo es para confirmar que las variables estén en minúsculas y sin acentos
print("Vacaciones: ", vacaciones_minuscula)
print("Descanso: ", descanso_minuscula)

#Este es el algoritmo para verificar si el padre puede o no asistir al juego de su hijo
if vacaciones_minuscula == "si" or descanso_minuscula == "si":
    print("Sí puede asistir al juego de su hijo")
elif vacaciones_minuscula == "no" or descanso_minuscula == "no":
    print("No puede asistir al juego de su hijo")
else:
    print("Opción errónea")