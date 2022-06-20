class Figura_Geometrica:
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

#Métodos getter y setter para "alto"
    def set_alto(self, alto):
        self.__alto = alto

    def get_alto(self):
        return self.__alto

#Métodos getter y setter para "ancho"
    def set_ancho(self, ancho):
        self.__ancho = ancho

    def get_ancho(self):
        return self.__ancho

#Método str para imprimir información
    def __str__(self):
        return f"Alto: {self.get_alto()} - Ancho {self.get_ancho()}"

#print(Figura_Geometrica.mro())

"""figura_1 = Figura_Geometrica(None, None)
figura_1.set_alto(float(input("Alto de la figura: ")))
figura_1.set_ancho(float(input("Ancho de la figura: ")))
print(figura_1)"""