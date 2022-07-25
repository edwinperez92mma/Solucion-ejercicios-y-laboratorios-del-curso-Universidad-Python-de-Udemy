from logger_base import log

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

#Método str para imprimir el estado del objeto "Usuario"
    def __str__(self):
        return f"Id usuario: {self._id_usuario} - Username: {self._username} - Password: {self._password}"

#Métodos getter y setter para "id_usuario"
    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

#Métodos getter y setter para "username"
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

#Métodos getter y setter para "password"
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

#Zona de pruebas
if __name__ == "__main__":
    usuario_1 = Usuario(1, "eperezb", "123")
    log.debug(usuario_1)

    #Simular un insert
    usuario_1 = Usuario(username="eperezb", password="123")
    log.debug(usuario_1)

    #Simular un delete
    usuario_1 = Usuario(id_usuario=1)
    log.debug(usuario_1)