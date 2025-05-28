# EJERCICIO 14
'''
Pide al usuario su peso en kilogramos y su altura en metros. 
Calcula el IMC (IMC = peso / (altura * altura)) y clasifícalo según las siguientes categorías:
•   Menos de 18.5: Bajo peso
•   18.5 a 24.9: Peso normal
•   25.0 a 29.9: Sobrepeso
•   30.0 o más: Obesidad
'''

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
clasificacion = ""
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
print(f"IMC: {imc:.1f} - {clasificacion}")