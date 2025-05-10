# Generador de números primos hasta N (3 casos fijos)
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primos_hasta(n):
    return [i for i in range(2, n+1) if es_primo(i)]

# Caso 1: N = 10
print("Primos hasta 10:", primos_hasta(10))

# Caso 2: N = 50
print("Primos hasta 50:", primos_hasta(50))

# Caso 3: N = 24
print("Primos hasta 24:", primos_hasta(24))
