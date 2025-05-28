# EJERCICIO 13
'''
Define un diccionario que represente un inventario con nombres de productos como claves y sus cantidades como valores
(ej. {"Arroz": 15, "Azúcar": 3, "Sal": 8, "Aceite": 2}). 
Recorre el diccionario y muestra solo los productos que tienen bajo stoc'''

inventario = {"Arroz": 15, "Azúcar": 3, "Sal": 8, "Aceite": 2}
print("Productos con bajo stock:")
for producto, cantidad in inventario.items():
    if cantidad <= 5:
        print(f"- {producto}: {cantidad} unidades")