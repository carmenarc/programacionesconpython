# Función para leer el contenido de un archivo
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

# Función para escribir en un archivo
def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

# Función para recorrer secuencialmente un archivo y detectar EOF (fin de archivo)
def recorrer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        while True:
            linea = archivo.readline()
            if not linea:  # Si la línea es vacía, se alcanzó EOF
                break
            print(linea, end='')

# Archivo de entrada y salida
archivo_entrada = "entrada.txt"
archivo_salida = "salida.txt"

# Escribir en el archivo de entrada
texto = "Este es un texto de ejemplo que será escrito en el archivo."
escribir_archivo(archivo_entrada, texto)
print("El contenido se ha escrito en el archivo de entrada:", archivo_entrada)

# Leer el contenido del archivo de entrada
contenido_leido = leer_archivo(archivo_entrada)
print("Contenido del archivo de entrada:")
print(contenido_leido)

# Escribir el contenido del archivo de entrada en el archivo de salida
escribir_archivo(archivo_salida, contenido_leido.upper())
print("El contenido se ha escrito en el archivo de salida:", archivo_salida)

# Recorrer secuencialmente el archivo de salida
print("Recorrido secuencial del archivo de salida:")
recorrer_archivo(archivo_salida)

