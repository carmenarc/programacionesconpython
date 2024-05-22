# Ejemplo de variables globales y locales
variable_global = 10

def funcion1():
    variable_local = 20
    print("Dentro de la función: variable_local =", variable_local)
    print("Dentro de la función: variable_global =", variable_global)

funcion1()
print("Fuera de la función: variable_global =", variable_global)

# Ejemplo de funciones anidadas
def funcion_anidada():
    print("String en la función anidada.")

def funcion2():
    print("Llamando a la primera función:")
    funcion_anidada()

funcion2()
