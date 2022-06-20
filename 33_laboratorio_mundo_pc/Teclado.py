from Dispositivo_Entrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        super().__init__(marca, tipo_entrada)
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados

#Método str para imprimir los detalles del objeto
    def __str__(self):
        return f"Id: {self.__id_teclado} - {super().__str__()}"

#Pruebas de creación de objeto de tipo "Teclado" que solo aparecen en consola si se ejecutan desde este archivo
if __name__ == "__main__":
    teclado_1 = Teclado("marca generica", "usb")
    print(teclado_1)
    teclado_2 = Teclado("redragon", "usb")
    #teclado_2.marca = "hp"
    #teclado_2.tipo_entrada = "ps2"
    print(teclado_2)