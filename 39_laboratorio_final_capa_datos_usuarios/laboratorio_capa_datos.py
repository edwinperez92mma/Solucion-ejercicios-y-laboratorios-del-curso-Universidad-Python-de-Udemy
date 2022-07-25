print("Laboratorio Final Capa Datos Usuarios")
#Revisar la imagen jpg para ver todas las clases con sus atributos y métodos.

#1.Las clases "Conexion" y "CursorDelPool" las podemos reutilizar del anterior proyecto.

#2.Debemos crear una tabla llamada "usuario" con los siguientes campos:
"""
id_usuario (data type: serial - Not Null?: yes - primary key?: yes)
username (data type: character varying - Not Null?: yes - primary key?: no)
password (data type: character varying - Not Null?: yes - primary key?: no)
"""
#La configuración de la tabla debe ser:
"""
Pestaña: "General"
Name: usuario
Owner: postgres
Schema: public
"""
#Le agregamos un par de usuarios manualmente desde pgAdmin.

#3.Tenemos que crear una clase "Usuario" que vendría a ser la clase "Persona" del proyecto anterior.

#4.La clase "UsuarioDao" es la que permite ejecutar las sentencias SQL, vendría a ser la clase "PersonaDao" del proyecto anterior.

#5."MenuAppUsuario" no es una clase sino un archivo que contiene el menú para elegir las opciones CRUD desde consola. El menú debe lucir así:
"""
Opciones:
1.Listar usuarios
2.Agregar usuario
3.Modificar usuario
4.Eliminar usuario
5.Salir
Escribe tu opción (1-5):
"""
#Ver la otra imagen jpg para más información sobre el menú.

#6.El archivo "logger_base" es prácticamente el mismo del proyecto anterior. La idea es usar "log" esto y no "print". 