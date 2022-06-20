from Producto import *

class Orden:

    contador_orden = 0

    def __init__(self, productos):
        Orden.contador_orden += 1
        self.__id_orden = Orden.contador_orden
        self.__lista_productos = list(productos)

#Método para agregar productos a la orden, posterior a la creación de la orden
    def agregar_productos(self, producto):
        self.__lista_productos.append(producto)

    def calcular_total(self):
        total = 0
        for i in self.__lista_productos:
            total += i.precio
        return total

#Método str para imprimir detalles de los productos
    def __str__(self):
        productos_str = ""
        for i in self.__lista_productos:
            productos_str += i.__str__() + "|"
        return f"Id Orden: {self.__id_orden} \nProductos: {productos_str}"

if __name__ == "__main__":
    producto_1 = Producto("pantalón", 90000)
    producto_2 = Producto("camisa", 50000)
    lista_1 = [producto_1, producto_2]
    orden_1 = Orden(lista_1)
    print(orden_1)
    lista_2 = [producto_1, producto_2]
    orden_2 = Orden(lista_2)
    print(orden_2)