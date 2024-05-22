def dividir(a, b):
    try:
        resultado = a / b
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    finally:
        print("¡Gracias por usar nuestro programa!")

# Ejemplo de lanzamiento de excepción
print("Ejemplo de lanzamiento de excepción:")
dividir(10, 0)

# Ejemplo de captura de excepción
print("\nEjemplo de captura de excepción:")
dividir(10, 2)
