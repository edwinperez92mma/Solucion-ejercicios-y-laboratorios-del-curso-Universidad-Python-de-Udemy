from logger_base import log

class Videojuego:
    def __init__(self, id_videojuego=None, nombre=None, genero=None, desarrolladora=None, plataforma=None, año=None):
        self._id_videojuego = id_videojuego
        self._nombre = nombre
        self._genero = genero
        self._desarrolladora = desarrolladora
        self._plataforma = plataforma
        self._año = año

#Método str para imprimir el estado del objeto
    def __str__(self):
        return f"""
            Id videojuego: {self._id_videojuego} - Nombre: {self._nombre} - Género: {self._genero}
            Desarrolladora: {self._desarrolladora} - Plataforma: {self._plataforma} - Año: {self._año}
        """

#Métodos getter y setter para "id_videojuego"
    @property
    def id_videojuego(self):
        return self._id_videojuego
    
    @id_videojuego.setter
    def id_videojuego(self, id_videojuego):
        self._id_videojuego = id_videojuego

#Métodos getter y setter para "nombre"
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

#Métodos getter y setter para "genero"
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero

#Métodos getter y setter para "desarrolladora"
    @property
    def desarrolladora(self):
        return self._desarrolladora
    
    @desarrolladora.setter
    def desarrolladora(self, desarrolladora):
        self._desarrolladora = desarrolladora

#Métodos getter y setter para "plataforma"
    @property
    def plataforma(self):
        return self._plataforma

    @plataforma.setter
    def plataforma(self, plataforma):
        self.plataforma = plataforma

#Métodos getter y setter para "año"
    @property
    def año(self):
        return self._año
    
    @año.setter
    def año(self, año):
        self._año = año

if __name__ == "__main__":
    videojuego_1 = Videojuego(1, "Resident Evil", "Survival Horror", "Capcom", "Play Station", 1998)
    log.debug(videojuego_1)

    #Simular un insert
    videojuego_1 = Videojuego(nombre="Resident Evil", genero="Survival Horror", desarrolladora="Capcom", plataforma="Play Station", año=1998)
    log.debug(videojuego_1)

    #Simular un delete
    videojuego_1 = Videojuego(id_videojuego=1)
    log.debug(videojuego_1)