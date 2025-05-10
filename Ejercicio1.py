def suma_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(3)] for i in range(3)]

def imprimir_matriz(m):
    for fila in m:
        print(fila)
    print()

# Caso de prueba 1
A1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B1 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Caso 1: A + B")
imprimir_matriz(suma_matrices(A1, B1))

# Caso de prueba 2
A2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B2 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print("Caso 2: A + B")
imprimir_matriz(suma_matrices(A2, B2))

# Caso de prueba 3
A3 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
B3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
print("Caso 3: A + B")
imprimir_matriz(suma_matrices(A3, B3))
