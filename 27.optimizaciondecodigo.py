# Función para calcular el número de Fibonacci de forma recursiva (sin optimización)
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Función para calcular el número de Fibonacci utilizando memoización
def fibonacci_memoizacion(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoizacion(n-1, memo) + fibonacci_memoizacion(n-2, memo)
    return memo[n]

# Ejemplo de uso del programa optimizado
n = 10

print("Calculando Fibonacci de", n, "de forma recursiva:")
print(fibonacci_recursivo(n))

print("\nCalculando Fibonacci de", n, "utilizando memoización:")
print(fibonacci_memoizacion(n))
