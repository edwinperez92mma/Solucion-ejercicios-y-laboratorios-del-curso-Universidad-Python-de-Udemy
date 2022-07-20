from logger_base import log

class Videojuego:
    def __init__(self, id_videojuego=None, nombre=None, genero=None, desarrolladora=None, plataforma=None, año=None):
        self.__id_videojuego = id_videojuego
        self.__nombre = nombre
        self.__genero = genero
        self.__desarrolladora = desarrolladora
        self.__plataforma = plataforma
        self.__año = año

    def __str__(self):
        return f"""
            Id_videojuego: {self.__id_videojuego}, Nombre: {self.__nombre},
            Genero: {self.__genero}, Desarrolladora: {self.__desarrolladora},
            Plataforma: {self.__plataforma}, Año: {self.__año}
        """

#Getter y Setter para "id_videojuego"
    @property
    def id_videojuego(self):
        return self.__id_videojuego
    
    @id_videojuego.setter
    def id_videojuego(self, id_videojuego):
        self.__id_videojuego = id_videojuego

#Getter y Setter para "nombre"
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

#Getter y Setter para "genero"
    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, genero):
        self.__genero = genero

#Getter y Setter para "desarrolladora"
    @property
    def desarrolladora(self):
        return self.__desarrolladora

    @desarrolladora.setter
    def desarrolladora(self, desarrolladora):
        self.__desarrolladora = desarrolladora

#Getter y Setter para "plataforma"
    @property
    def plataforma(self):
        return self.__plataforma

    @plataforma.setter
    def plataforma(self, plataforma):
        self.__plataforma = plataforma

#Getter y Setter para "año"
    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, año):
        self.__año = año

#Pruebas de creación de objetos "videojuego"

if __name__ == "__main__":
    videojuego_1 = Videojuego(1, "Resident Evil 3", "Survival Horror", "Capcom", "Play Station", 1999)
    log.debug(videojuego_1)

#Simular un insert
    videojuego_1 = Videojuego(nombre="Resident Evil 3", genero="Survival Horror", desarrolladora="Capcom", plataforma="Play Station", año=1999)
    log.debug(videojuego_1)

#Simular un delete
    videojuego_1 = Videojuego(id_videojuego=1)
    log.debug(videojuego_1)