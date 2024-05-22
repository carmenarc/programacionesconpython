# Función que suma dos números y devuelve el resultado
def suma(a, b):
    return a + b

# Procedimiento que imprime un mensaje de saludo
def saludar(nombre):
    print("¡Hola,", nombre, "!")

# Función que modifica una lista
def modificar_lista(lista):
    lista.append(4)  # Agregar un elemento a la lista

# Procedimiento que imprime todos los elementos de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento, end=' ')
    print()

# Ejemplos de llamadas a las funciones y procedimientos
resultado_suma = suma(3, 5)
print("Resultado de la suma:", resultado_suma)

saludar("Juan")

mi_lista = [1, 2, 3]
print("Lista original:")
imprimir_lista(mi_lista)

modificar_lista(mi_lista)
print("Lista después de modificarla:")
imprimir_lista(mi_lista)

# Parámetros por valor
x = 10

def cambiar_valor(num):
    num = 20  # Cambiando el valor de la variable local num

cambiar_valor(x)
print("Valor de x después de llamar a la función:", x)  # x sigue siendo 10

# Parámetros por referencia
mi_lista = [1, 2, 3]

def modificar_lista(lista):
    lista.append(4)

modificar_lista(mi_lista)
print("Lista después de llamar a la función:", mi_lista)  # mi_lista ahora tiene un elemento más
