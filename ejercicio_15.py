# EJERCICIO 15
'''
Pide al usuario que ingrese la temperatura (en grados Celsius) para cada uno de los 7 días de la semana.
Al finalizar, el programa debe mostrar la temperatura promedio, la temperatura más alta y la temperatura más baja registrada.'''

temperaturas = []
for dia in range(1, 8):
    temp = float(input(f"Temperatura día {dia}: "))
    temperaturas.append(temp)
print(f"Promedio: {sum(temperaturas)/7:.1f}°C")
print(f"Máxima: {max(temperaturas)}°C | Mínima: {min(temperaturas)}°C")