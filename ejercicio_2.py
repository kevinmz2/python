# EJERCICIO 2
'''
Escribe un programa que solicite la edad de una persona y determine si su voto es "Obligatorio" (18-65 años), 
"Facultativo" (16-17 años y mayores de 65 años), o si "Aún no puede votar" (menores de 16 años)'''

edad = int(input("Ingresa tu edad: "))
if 18 <= edad <= 65:
    print("tu voto es obligatorio")
elif 16 <= edad < 18 or edad > 65:
    print("tu voto es facultativo")
else:
    print("lo siento, no puedes votar")