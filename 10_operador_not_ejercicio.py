print("Operador not - ejercicio")
#Se trata del ejercicio anterior, pero invirtiendo las condicionales. Es decir, si no son vacaciones, ni es día de descanso, el padre no puede
#asisitir al juego de su hijo

vacaciones = False
descanso = False

if not (vacaciones or descanso):
    print("No puede asistir al juego de su hijo")
else:
    print("Sí puede asistir al juego de su hijo")