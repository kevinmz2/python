# EJERCICIO 3
'''
Desarrolla un programa que pida las tres notas parciales de un estudiante, 
calcule su promedio y muestre si el estudiante "Aprobó" o "Reprobó'''

nota1 = float(input("Ingresa nota 1: "))
nota2 = float(input("Ingresa nota 2: "))
nota3 = float(input("Ingresa nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"tu promedio: {promedio:.1f} - {'Aprobó' if promedio >= 7.0 else 'Reprobó'}")