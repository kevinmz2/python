# EJERCICIO 4
'''
Crea un programa que pida al usuario una cantidad en USD y la moneda a la que desea convertir (EUR, GBP, JPY). 
Luego, usando tasas de cambio fijas (ej. 1 USD =0.92 EUR, 1 USD = 0.79 GBP, 1 USD = 156.40 JPY), 
muestre la cantidad convertida
'''

usd = float(input("Monto en USD: "))
moneda = input("Convertir a (EUR/GBP/JPY): ").upper()
tasas = {"EUR": 0.92, "GBP": 0.79, "JPY": 156.40}
if moneda in tasas:
    print(f"{usd} USD = {usd * tasas[moneda]:.2f} {moneda}")
else:
    print("Moneda no válida.")