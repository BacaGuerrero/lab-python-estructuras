# Búsqueda lineal en una lista con casos codificados
def buscar_elemento(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i
    return -1

arreglo = [3, 8, 15, 23, 42, 7, 9, 14, 29, 31]

# Caso 1: Buscar 15
resultado = buscar_elemento(arreglo, 15)
print("Buscar 15:", "Posición", resultado if resultado != -1 else "No encontrado")

# Caso 2: Buscar 100
resultado = buscar_elemento(arreglo, 100)
print("Buscar 100:", "Posición", resultado if resultado != -1 else "No encontrado")

# Caso 3: Buscar 3
resultado = buscar_elemento(arreglo, 3)
print("Buscar 3:", "Posición", resultado if resultado != -1 else "No encontrado")
