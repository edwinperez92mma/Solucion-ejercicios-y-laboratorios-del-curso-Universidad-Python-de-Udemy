print("Laboratorio Mundo PC")
#Nota antes de ver la imagen: el atributo "tamaño" de la clase "Monitor", es de tipo string. En la imagen sale que es de tipo "Monitor" pero eso es un
#error.
#Nota 2 antes de ver la imagen: los atributos privados (-) llevan doble guion bajo (__) y se acceden y modifican con getters y setters.
#Nota 3 antes de ver la imagen: los atributos protegidos (#) llevan un guion bajo (_).
#Ver la imagen .jpg para todos los detalles de cómo deben ser los módulos de nuestro programa.

#Clase "Orden":
"""
Nombre: 
Orden

Atributos:
+ contadorOrdenes: int <<static>> - Para saber cuántas órdenes se han creado.
- idOrden: int - un identificador único dependiendo del atributo contadorOrdenes por cada objeto "orden" que se cree.
- computadoras: List<Computadora> - se recibe desde el constructor o el init de la clase "Orden".

Métodos:
+ agregarComputadoras(computadora) - método para añadir más elementos a la lista "computadoras" además de las que se reciben en el constructor.
+ __str__() - para desplegar la información de las computadoras añadidas a nuestra orden.
+ métodos get/set para cada atributo.

Responsabilidades:
Crea objetos de tipo "Orden" y almacena en una lista los objetos de tipo "Computadora".
"""

#Clase "Computadora" (tiene una relación de agregación con la clase "Orden"):
"""
Nombre: Computadora

Atributos:
+ contadorComputadoras: int <<static>>
- idComputadora: int
- nombre: string
- monitor: Monitor - atributo de tipo Monitor, es decir es un objeto creado a partir de la clase Monitor.
- teclado: Teclado - atributo de tipo Teclado.
- raton: Raton - atributo de tipo Raton.

Métodos:
+ __str__()
+ métodos get/set para cada atributo.

Responsabilidades:
Crea objetos de tipo "Computadora", incluyendo su "nombre", y se le adjuntan los objetos de tipo Monitor, Teclado y Computador.
Los objetos de tipo "Computadora" se agregarán a los objetos de tipo "Orden", la clase "Orden" los almacenará por medio del atrbuto (lista)
computadoras.
"""

#La clase computadora a su vez está compuesta de otas clases: "Monitor", "Raton" y "Teclado". Y a su vez, las clases "Raton" y "Teclado" tienen
#una clase padre llamada "DispositivoEntrada"

#Clase "Monitor" (tiene una relación de agregación con la clase "Computadora"):
"""
Nombre: Monitor

Atributos:
+ contadorMonitores: int <<static>>
- idMonitor: int
- marca: string
- tamaño: string

Métodos:
+ __str__()
+ métodos get/set para cada atributo.

Responsabilidades:
Crea objetos de tipo "Monitor".
"""

#Clase "DispositivoEntrada" (es la clase padre de las subclases "Raton" y "Teclado", tienen relación de herencia):
"""
Nombre: DispositivoEntrada

Atributos:
# tipoEntrada: string - el numeral indica que son de tipo protegidos, osea que sean accedidos directamente por las clases hijas de esos atributos.
# marca: string

Métodos:
+ __str__()
+ métodos get/set para cada atributo.

Responsabilidades:
Crea objetos de tipo "DispositivoEntrada".
"""

#Clase "Raton" (clase hija de "DispositivoEntrada", tiene una relación de agregación con la clase "Computadora")
"""
Nombre: Raton

Atributos:
+ contadorRatones: int <<static>>
- idRaton: int

Métodos:
+ __str__()

Responsabilidades:
Crea objetos de tipo "Raton".
"""

#Clase "Teclado" (clase hija de "DispositivoEntrada", tiene una relación de agregación con la clase "Computadora")
"""
Nombre: Teclado

Atributos:
+ contadorTeclados: int <<static>>
- idTeclado: int

Métodos:
+ __str__()

Responsabilidades:
Crea objetos de tipo "Teclado".
"""

#Finalmente crearemos una clase de tipo "Prueba" para ensayar la creación de objetos de tipo "Orden", "Computadora", y llenar los objetos de tipo
#computadora con objetos de tipo "Monitor", "Raton" y "Teclado".

#Se recomienda empezar creando las clases que tienen menos dependencias con otras clases. El orden recomendado es:
#1.DispositivoEntrada
#2.Raton
#3.Teclado
#4.Monitor
#5.Computadora
#6.Orden
#Tambiés es recomendable ir creando objetos dentro de cada clase a medida que se van realizando las clases, para verificar que funcionen.
#No olvidar que en "Orden" hay que crear una lista de objetos "Computadora". Estos objetos se pasan a Orden por medio del init.

#Orden recomendado de creación de objetos:
#1.Raton
#2.Teclado
#3.Monitor
#4.Computadora

#5.Orden - se crean los objetos de tipo "Orden" luego de tener varios objetos de tipo computadora creados.

#El objeto orden imprimir todos los datos de las computadoras, debe lucir así:
"""
Orden: 1, computadoras:
        Hp: 1
            Monitor: Id: 1, marca: Hp, tamaño: 15 pulgadas
            Teclado: Id: 1, marca: Hp, tipo_entrada: usb
            Ratón: Id: 1, marca: Hp, tipo_entrada: usb

        Acer: 2
            Monitor: Id: 2, marca: Acer, tamaño: 27 pulgadas
            Teclado: Id: 2, marca: Acer, tipo_entrada: bluetooth
            Ratón: Id: 2, marca: Acer, tipo_entrada: bluetooth

Orden: 2, computadoras:
        Gamer: 3
            Monitor: Id: 3, marca: Gamer, tamaño: 45 pulgadas
            Teclado: Id: 3, marca: Gamer, tipo_entrada: bluetooth
            Ratón: Id: 3, marca: Gamer, tipo_entrada: bluetooth

        Hp: 1
            Monitor: Id: 1, marca: Hp, tamaño: 15 pulgadas
            Teclado: Id: 1, marca: Hp, tipo_entrada: usb
            Ratón: Id: 1, marca: Hp, tipo_entrada: usb

"""