# EJERCICIO 6
'''
Simula un cajero automático con un saldo inicial fijo (ej. $500). 
Permite al usuario intentar retirar dinero. Si el monto es válido (múltiplo de 5 o 10) y hay saldo, realiza el retiro y actualiza el saldo. 
Si no, muestra un mensaje de error. Permite múltiples retiros hasta que el usuario decida salir o el saldo sea insuficiente'''

saldo = 500
while True:
    print(f"\nSaldo actual: ${saldo}")
    monto = float(input("Monto a retirar (0 para salir): "))
    if monto == 0:
        break
    if monto % 5 != 0 and monto % 10 != 0:
        print("Error: El monto debe ser múltiplo de 5 o 10.")
    elif monto > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= monto
        print("Retiro exitoso.")