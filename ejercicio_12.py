# EJERCICIO 12
'''
El programa debe "pensar" en un número aleatorio entre 1 y 20. El usuario tiene 5 intentos para adivinarlo. 
Después de cada intento, el programa debe indicar si el número adivinado es "Demasiado alto", "Demasiado bajo" o "Correcto". 
Si el usuario adivina, el juego termina. Si agota los intentos, se revela el número'''

import random
numero_secreto = random.randint(1, 20)
intentos = 5
while intentos > 0:
    guess = int(input("Adivina (1-20): "))
    if guess == numero_secreto:
        print("¡Correcto!")
        break
    print("Demasiado alto" if guess > numero_secreto else "Demasiado bajo")
    intentos -= 1
else:
    print(f"¡Perdiste! Era el {numero_secreto}.")