print("Calculadora de impuestos - ejercicio")
"""
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado
Fórmula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

Ejemplo:
Proporcione el pago sin impuesto: 1000
Proporcione el monto del impuesto: 16

Pago con impuesto: 1160.0
"""

"""
def calculadora_impuestos():
    pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
    monto_del_impuesto = float(input("Monto del impuesto: "))
    print(f"Pago con impuesto: {pago_sin_impuesto + pago_sin_impuesto * (monto_del_impuesto/100)}")

calculadora_impuestos()
"""
print("Solución propuesta por el instructor")

def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
monto_del_impuesto = float(input("Proporcione el monto del impuesto: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto,monto_del_impuesto)
print(f"Pago con impuesto: {pago_con_impuesto}")