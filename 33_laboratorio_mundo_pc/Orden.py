from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from Computadora import Computadora

class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = list(computadoras)

#Métedos getter y setter para atributo "computadoras"
    @property
    def computadoras(self):
        return self.__computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self.__computadoras = computadoras

#Método para agregar computadoras a una orden ya creada
    def agregar_computadoras(self, computadora):
        self.__computadoras.append(computadora)

#Método str para imprimir los detalles del objeto
    def __str__(self):
        computadoras_str = ""
        for i in self.__computadoras:
            computadoras_str += i.__str__() + "\n"
        return f"\nOrden: {self.__id_orden}, computadoras:\n{computadoras_str}"

#Pruebas de creación de objeto de tipo "Computadora" que solo aparecen en consola si se ejecutan desde este archivo
if __name__ == "__main__":
    monitor_1 = Monitor("LG", "30")
    teclado_1 = Teclado("Redragon", "usb")
    raton_1 = Raton("esenses", "usb")
    computadora_1 = Computadora("PC Gamer", monitor_1, teclado_1, raton_1)

    monitor_2 = Monitor("Samsung", "50")
    teclado_2 = Teclado("Razer", "usb")
    raton_2 = Raton("logitech", "usb")
    computadora_2 = Computadora("PC de Edicion", monitor_2, teclado_2, raton_2)

    monitor_3 = Monitor("LG", "21")
    teclado_3 = Teclado("Genius", "ps2")
    raton_3 = Raton("Genius", "ps2")
    computadora_3 = Computadora("PC economico", monitor_3, teclado_3, raton_3)

    lista_computadoras = [computadora_1, computadora_2, computadora_3]
    orden_1 = Orden(lista_computadoras)
    print(orden_1)

    orden_2 = Orden(lista_computadoras)
    print(orden_2)