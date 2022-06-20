from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor

class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

#Métedos getter y setter para atributo "nombre"
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

#Métedos getter y setter para atributo "monitor"
    @property
    def monitor(self):
        return self.__monitor
    
    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

#Métedos getter y setter para atributo "teclado"
    @property
    def teclado(self):
        return self.__teclado
    
    @teclado.setter
    def teclado(self, teclado):
        self.__teclado = teclado

#Métedos getter y setter para atributo "raton"
    @property
    def raton(self):
        return self.__raton
    
    @raton.setter
    def raton(self, raton):
        self.__raton = raton

#Método str para imprimir los detalles del objeto
    def __str__(self):
        return f"{self.__nombre}: {self.__id_computadora} \nMonitor: {self.__monitor} \nTeclado: {self.__teclado} \nRaton: {self.__raton}"

#Pruebas de creación de objeto de tipo "Computadora" que solo aparecen en consola si se ejecutan desde este archivo
if __name__ == "__main__":
    monitor_1 = Monitor("LG", "30")
    teclado_1 = Teclado("Redragon", "usb")
    raton_1 = Raton("esenses", "usb")
    computadora_1 = Computadora("PC Gamer", monitor_1, teclado_1, raton_1)
    print(computadora_1)

    monitor_2 = Monitor("Samsung", "50")
    teclado_2 = Teclado("Razer", "usb")
    raton_2 = Raton("logitech", "usb")
    computadora_2 = Computadora("PC de Edicion", monitor_2, teclado_2, raton_2)
    print(computadora_2)

    monitor_3 = Monitor("LG", "21")
    teclado_3 = Teclado("Genius", "ps2")
    raton_3 = Raton("Genius", "ps2")
    computadora_3 = Computadora("PC economico", monitor_3, teclado_3, raton_3)
    print(computadora_3)