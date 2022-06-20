class Monitor:

    contador_monitores = 0

    def __init__(self, marca, tamanho):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = marca
        self.__tamanho = tamanho

#Métedos getter y setter para atributo "marca"
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

#Métedos getter y setter para atributo "tamanho"
    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self.__tamanho = tamanho

#Método str para imprimir los detalles del objeto
    def __str__(self):
        return f"Id: {self.__id_monitor} - Marca: {self.__marca} - Tamaño: {self.__tamanho} pulgadas"

#Pruebas de creación de objeto de tipo "Monitor" que solo aparecen en consola si se ejecutan desde este archivo
if __name__ == "__main__":
    monitor_1 = Monitor("LG", "30")
    print(monitor_1)
    monitor_2 = Monitor("Samsung", "50")
    #monitor_2.marca = "generico"
    #monitor_2.tamanho = "16"
    print(monitor_2)