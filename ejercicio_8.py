# EJERCICIO 8
'''
Pide al usuario que ingrese una palabra. 
El programa debe contar y mostrar cuántas vocales (a, e, i, o, u, mayúsculas y minúsculas) contiene esa palabra.'''
palabra = input("Ingresa una palabra: ").lower()
vocales = {'a', 'e', 'i', 'o', 'u'}
contador = sum(1 for letra in palabra if letra in vocales)
print(f"La palabra tiene {contador} vocal(es).")