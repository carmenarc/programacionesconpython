class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.ocupacion}.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz cumpleaños! Ahora tengo {self.edad} años.")

# Crear objetos de la clase Persona
persona1 = Persona("Juan", 30, "ingeniero")
persona2 = Persona("María", 25, "estudiante")

# Llamar al método presentarse de cada objeto
persona1.presentarse()
persona2.presentarse()

# Llamar al método cumplir_anios para persona1
persona1.cumplir_anios()
