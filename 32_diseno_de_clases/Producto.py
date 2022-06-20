class Producto:

    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self.__id_producto = Producto.contador_producto
        self.__nombre = nombre
        self.__precio = precio

#Método getter para precio
    @property
    def precio(self):
        return self.__precio

#Método str para imprimir detalles de los productos
    def __str__(self):
        return f"Id producto: {self.__id_producto}, Nombre: {self.__nombre}, Precio: {self.__precio}"

if __name__ == "__main__":
    producto_1 = Producto("pantalón", 90000)
    print(producto_1)

    producto_2 = Producto("camisa", 50000)
    print(producto_2)