class Dispositivo_Entrada:
    def __init__(self, marca, tipo_entrada):
        self.__marca = marca
        self.__tipo_entrada = tipo_entrada

#Métedos getter y setter para atributo "marca"
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

#Métedos getter y setter para atributo "tipo_entrada"
    @property
    def tipo_entrada(self):
        return self.__tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self.__tipo_entrada = tipo_entrada

#Método str para imprimir los detalles del objeto
    def __str__(self):
        return f"Marca: {self.__marca} - Tipo entrada: {self.__tipo_entrada}"

#Pruebas de creación de objeto de tipo "Dispositivo_Entrada" que solo aparecen en consola si se ejecutan desde este archivo
if __name__ == "__main__":
    dispositivo_entrada_1 = Dispositivo_Entrada("esenses", "usb")
    #dispositivo_entrada_1.marca = "razer"
    #dispositivo_entrada_1.tipo_entrada = "ps2"
    print(dispositivo_entrada_1)