from Bicicleta import Bicicleta
from Coche import Coche
from Vehiculo import Vehiculo

print("\nObjeto Vehículo")
vehiculo_1 = Vehiculo("Azul", 4)
#Impresión del método str
print(vehiculo_1)
#Impresión del getter para kilómetros
#print(f"Color: {vehiculo_1.get_color()} - Ruedas: {vehiculo_1.get_ruedas()}\n")

print("\nObjeto Coche")
#Objeto coche de la clase Vehiculo
coche_1 = Coche("rojo", 4, 0)
#Impresión del método str
print(coche_1)
#Impresión del getter para kilómetros
#print(f"Kilómetros: {coche_1.get_kilometros()}\n")

print("\nObjeto Bicicleta")
#Objeto bicicleta de la clase Vehiculo
bicicleta_1 = Bicicleta("Verde", 2, "Ruta")
#Impresión del método str
print(bicicleta_1)
#Impresión del getter para tipo
#print(f"Tipo: {bicicleta_1.get_tipo()}")