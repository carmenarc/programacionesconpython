# Creación de un array
mi_array = [10, 20, 30, 40, 50]

# Acceso a elementos del array
print("Elemento en la posición 0:", mi_array[0])
print("Elemento en la última posición:", mi_array[-1])

# Modificación de un elemento del array
mi_array[2] = 35
print("Array después de modificar el elemento en la posición 2:", mi_array)

# Recorrido del array
print("Recorrido del array:")
for elemento in mi_array:
    print(elemento)

# Otra forma de recorrer el array utilizando índices
print("\nRecorrido del array utilizando índices:")
for i in range(len(mi_array)):
    print("Elemento en la posición", i, ":", mi_array[i])
