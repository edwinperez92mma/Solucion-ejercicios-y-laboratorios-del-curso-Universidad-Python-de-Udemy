print("Diseño de clases")
#Vamos a crear 2 clases: "Orden" y "Producto". Básicamente se trata de vender varios productos para ser agregados a una orden. Se calculará el precio
#total a partir de dla variable precio de la clase "Producto".

#La clase "Producto" será así:
"""
Nombre: 
Producto

Atributos:
+ contador_productos: int <<class variable>>
- id_producto: int (este tendrá un identificador único mediante una variable de clase, que en este caso será la de "contador_productos")
- nombre: str
- precio: float

Método:
+ __str__()
"""
#Por cada Producto creado, este será agregado a la clase orden. Serán agregados a una lista llamada "productos" en la clase "Orden".

#La clase "Orden" será así:
"""
Nombre: 
Orden

Atributos:
+ contador_ordenes: int <<class variable>>
- id_orden: int
- productos: <<Producto list>>

Método:
+ __str__()
"""
#Posteriormente se añadirán algunos métodos para agregar los productos extra, así como calcular el total de la venta