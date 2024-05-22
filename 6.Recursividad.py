def factorial(n):
    # Caso base: factorial de 0 es 1
    if n == 0:
        return 1
    # Caso recursivo: factorial de n es n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Ejemplo de uso de la función factorial
numero = 5
print("El factorial de", numero, "es:", factorial(numero))
