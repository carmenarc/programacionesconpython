# Función para invertir una cadena
def invertir_cadena(cadena):
    return cadena[::-1]

# Función para contar el número de palabras en una cadena
def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

# Función para verificar si una cadena es un palíndromo
def es_palindromo(cadena):
    cadena = cadena.lower()  # Convertir a minúsculas
    cadena = cadena.replace(' ', '')  # Eliminar espacios en blanco
    return cadena == cadena[::-1]

# Función para capitalizar la primera letra de cada palabra en una cadena
def capitalizar_palabras(cadena):
    palabras = cadena.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return ' '.join(palabras_capitalizadas)

# Ejemplo de uso del programa
cadena = "anita lava la tina"
print("Cadena original:", cadena)
print("Cadena invertida:", invertir_cadena(cadena))
print("Número de palabras:", contar_palabras(cadena))
print("¿Es un palíndromo?", es_palindromo(cadena))
print("Capitalizar palabras:", capitalizar_palabras(cadena))