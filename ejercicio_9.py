# EJERCICIO 9
'''
Crea un programa que pida al usuario un número y luego genere y muestre la tabla de multiplicar de ese número del 1 al 10'''

numero = int(input("Número para la tabla: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")