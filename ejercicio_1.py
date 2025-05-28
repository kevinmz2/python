#EJERCICIO 1
'''Crea un programa que pida al usuario el precio base de un producto y luego 
calcule y muestre el precio final con el 12% de IVA aplicado.'''

precio_base = float(input("Ingresa el precio base del producto: "))
iva = precio_base * 0.12
precio_final = precio_base + iva
print(f"el precio con IVA es: ${precio_final:.2f}")
