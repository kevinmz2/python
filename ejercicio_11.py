# EJERCICIO 11
'''
Pide al usuario su consumo de energía en kWh. Calcula y muestra el valor total de su factura eléctrica según estas tarifas.

'''

kwh = float(input("Consumo en kWh: "))
costo = 100 * 0.10 + max(kwh - 100, 0) * 0.15
print(f"Total a pagar: ${costo:.2f}")