def make_distinct(arr):
    # Ordenar el array
    arr.sort()
    operations = 0
    
    for i in range(1, len(arr)):
        # Si el elemento actual es menor o igual al anterior, necesitamos incrementarlo
        if arr[i] <= arr[i - 1]:
            operations += (arr[i - 1] - arr[i] + 1)
            arr[i] = arr[i - 1] + 1

    return operations

# Leer los valores de entrada
N = int(input())
A = list(map(int, input().split()))

# Calcular el número mínimo de operaciones
result = make_distinct(A)

# Imprimir el resultado
print(result)