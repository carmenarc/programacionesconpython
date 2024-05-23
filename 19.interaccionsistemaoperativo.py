import os

# Crear un directorio
os.makedirs("mi_directorio")

# Verificar si un directorio existe
if os.path.exists("mi_directorio"):
    print("El directorio 'mi_directorio' ha sido creado.")

# Escribir en un archivo
with open("mi_archivo.txt", "w") as f:
    f.write("¡Hola, mundo!\nEste es un archivo de prueba.")

# Leer un archivo
with open("mi_archivo.txt", "r") as f:
    contenido = f.read()
    print("\nContenido del archivo:")
    print(contenido)

# Listar archivos en el directorio actual
print("\nArchivos en el directorio actual:")
for archivo in os.listdir("."):
    print(archivo)

# Eliminar un archivo
os.remove("mi_archivo.txt")

# Eliminar un directorio
os.rmdir("mi_directorio")
