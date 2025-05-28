# EJERCICIO 10
'''
Pide al usuario una placa vehicular. Verifica y muestra si la placa ingresada cumple con el formato simplificado:
empieza con una letra, tiene 3 letras en total y luego 3 o 4 dígitos. (Ej: ABC1234 o PBA001).
'''
placa = input("Ingresa la placa (ej. ABC1234): ")
if (len(placa) == 6 or len(placa) == 7) and placa[:3].isalpha() and placa[3:].isdigit():
    print("Placa VÁLIDA")
else:
    print("Placa NO VÁLIDA")