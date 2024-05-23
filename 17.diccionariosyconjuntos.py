# diccionarios_y_conjuntos.py

# Crear un diccionario para almacenar información de estudiantes
estudiantes = {
    "Juan": {"edad": 20, "carrera": "Ingeniería"},
    "Ana": {"edad": 22, "carrera": "Derecho"},
    "Luis": {"edad": 21, "carrera": "Medicina"}
}

# Imprimir el diccionario de estudiantes
print("Diccionario de estudiantes:")
for nombre, info in estudiantes.items():
    print(f"{nombre}: {info}")

# Agregar un nuevo estudiante al diccionario
estudiantes["Maria"] = {"edad": 23, "carrera": "Arquitectura"}
print("\nDespués de agregar a Maria:")
print(estudiantes)

# Actualizar la información de un estudiante
estudiantes["Juan"]["edad"] = 21
print("\nDespués de actualizar la edad de Juan:")
print(estudiantes)

# Crear un conjunto para almacenar materias cursadas
materias = {"Matemáticas", "Física", "Química"}

# Imprimir el conjunto de materias
print("\nConjunto de materias:")
print(materias)

# Agregar una nueva materia al conjunto
materias.add("Biología")
print("\nDespués de agregar Biología:")
print(materias)

# Eliminar una materia del conjunto
materias.discard("Física")
print("\nDespués de eliminar Física:")
print(materias)

# Verificar la pertenencia de una materia en el conjunto
print("\n¿Está Química en el conjunto de materias?", "Química" in materias)
print("¿Está Física en el conjunto de materias?", "Física" in materias)

# Uso de diccionarios y conjuntos en funciones
def contar_estudiantes_por_carrera(estudiantes):
    contador = {}
    for info in estudiantes.values():
        carrera = info["carrera"]
        if carrera in contador:
            contador[carrera] += 1
        else:
            contador[carrera] = 1
    return contador

def materias_comunes(materias1, materias2):
    return materias1 & materias2

# Contar el número de estudiantes por carrera
contador_carreras = contar_estudiantes_por_carrera(estudiantes)
print("\nNúmero de estudiantes por carrera:")
print(contador_carreras)

# Ejemplo de uso de conjuntos para encontrar materias comunes
otras_materias = {"Matemáticas", "Historia", "Química"}
comunes = materias_comunes(materias, otras_materias)
print("\nMaterias comunes entre dos conjuntos:")
print(comunes)
