# EJERCICIO 5
'''
Pide al usuario el precio unitario de un producto y la cantidad comprada.
Calcula el total a pagar, aplicando el descuento si la cantidad es mayor a 100 unidades'''

precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad comprada: "))
total = precio_unitario * cantidad
if cantidad > 100:
    total *= 0.90  # 10% de descuento
print(f"Total a pagar: ${total:.2f}")