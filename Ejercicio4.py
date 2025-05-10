# Conversión de Celsius a Fahrenheit y Kelvin (3 casos fijos)
def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Caso 1
c1 = 25
f1, k1 = convertir_temperatura(c1)
print(f"Caso 1 - Celsius: {c1} → Fahrenheit: {f1}, Kelvin: {k1}")

# Caso 2
c2 = -10
f2, k2 = convertir_temperatura(c2)
print(f"Caso 2 - Celsius: {c2} → Fahrenheit: {f2}, Kelvin: {k2}")

# Caso 3
c3 = 100
f3, k3 = convertir_temperatura(c3)
print(f"Caso 3 - Celsius: {c3} → Fahrenheit: {f3}, Kelvin: {k3}")
