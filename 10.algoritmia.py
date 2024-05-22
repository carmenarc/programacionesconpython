# Función para encontrar el máximo de tres números
def encontrar_maximo(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3

# Entrada de los tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Encontrar el máximo de los tres números utilizando la función definida
maximo = encontrar_maximo(num1, num2, num3)

# Mostrar el resultado
print("El máximo de los tres números es:", maximo)
