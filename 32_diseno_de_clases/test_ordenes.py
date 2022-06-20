from Producto import Producto
from Orden import Orden

producto_1 = Producto("pantalón", 90000)
producto_2 = Producto("camisa", 50000)
producto_3 = Producto("bufanda", 15000)
producto_4 = Producto("guantes", 10000)

lista_1 = [producto_1, producto_2]
lista_2 = [producto_3, producto_4]

orden_1 = Orden(lista_1)
orden_1.agregar_productos(producto_3)
orden_1.agregar_productos(producto_4)
print(orden_1)
print(f"Total orden_1: {orden_1.calcular_total()}")

orden_2 = Orden(lista_2)
print(orden_2)
print(f"Total orden_2: {orden_2.calcular_total()}")