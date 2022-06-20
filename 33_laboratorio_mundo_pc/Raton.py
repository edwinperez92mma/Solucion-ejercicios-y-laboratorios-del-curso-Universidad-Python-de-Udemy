from Dispositivo_Entrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones

#Método str para imprimir los detalles del objeto
    def __str__(self):
        return f"Id: {self.__id_raton} - {super().__str__()}\n"

#Pruebas de creación de objeto de tipo "Raton" que solo aparecen en consola si se ejecutan desde este archivo
if __name__ == "__main__":
    raton_1 = Raton("esenses", "usb")
    print(raton_1)
    raton_2 = Raton("razer", "usb")
    #raton_2.marca = "esenses"
    #raton_2.tipo_entrada = "ps2"
    print(raton_2)