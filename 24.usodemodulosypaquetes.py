# operaciones.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    else:
        return a / b

if __name__ == "__main__":
    # Ejemplo de uso del módulo
    print("Ejemplo de uso del módulo operaciones:")
    print("5 + 3 =", suma(5, 3))
    print("5 - 3 =", resta(5, 3))
    print("5 * 3 =", multiplicacion(5, 3))
    print("5 / 3 =", division(5, 3))

