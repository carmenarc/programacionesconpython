# Definir la clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        print(f"Conduciendo un {self.marca} {self.modelo}")

# Definir una subclase de Vehiculo: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    # Sobrescribir el método conducir
    def conducir(self):
        print(f"Conduciendo un {self.color} {self.marca} {self.modelo} (Coche)")

# Definir otra subclase de Vehiculo: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada

    # Sobrescribir el método conducir
    def conducir(self):
        print(f"Conduciendo una {self.marca} {self.modelo} de {self.cilindrada} cc (Moto)")

# Crear instancias de las subclases y llamar al método conducir
coche = Coche("Toyota", "Corolla", "rojo")
moto = Moto("Honda", "CBR500R", 500)

coche.conducir()
moto.conducir()
