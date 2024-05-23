# diferencia_listas_tuplas.py

# Definiendo una lista y una tupla
mi_lista = [1, 2, 3, 4]
mi_tupla = (1, 2, 3, 4)

# Imprimiendo la lista y la tupla
print("Lista:", mi_lista)
print("Tupla:", mi_tupla)

# Demostrando mutabilidad de la lista
mi_lista[0] = 10
print("Lista después de modificar el primer elemento:", mi_lista)

# Intentando modificar la tupla (esto causará un error)
try:
    mi_tupla[0] = 10
except TypeError as e:
    print("Error al intentar modificar la tupla:", e)

# Iterando sobre la lista y la tupla
print("Iterando sobre la lista:")
for item in mi_lista:
    print(item)

print("Iterando sobre la tupla:")
for item in mi_tupla:
    print(item)

# Verificando pertenencia en la lista y la tupla
print("¿Está el 10 en la lista?", 10 in mi_lista)
print("¿Está el 2 en la tupla?", 2 in mi_tupla)

# Usando listas y tuplas en funciones
def procesar_secuencia(secuencia):
    suma = sum(secuencia)
    longitud = len(secuencia)
    return suma, longitud

# Procesando la lista y la tupla
suma_lista, longitud_lista = procesar_secuencia(mi_lista)
suma_tupla, longitud_tupla = procesar_secuencia(mi_tupla)

print("Resultados para la lista - Suma:", suma_lista, "Longitud:", longitud_lista)
print("Resultados para la tupla - Suma:", suma_tupla, "Longitud:", longitud_tupla)
