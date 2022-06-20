class Persona:
    contador_personas = 0
    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self.__id = Persona.contador_personas
        self.__nombre = nombre
        self.__edad = edad

#Getter y setter para nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

#Getter y setter para edad
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

#Getter y setter para id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, edad):
        self.__id = edad
    
    def __str__(self):
        return f"Nombre: {self.__nombre} - Edad: {self.__edad} - Id: {self.__id}"