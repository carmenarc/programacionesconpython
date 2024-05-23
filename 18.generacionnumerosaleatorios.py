import random

# a. Generar números aleatorios
numero_aleatorio = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
print("Número aleatorio generado:", numero_aleatorio)

# b. Simular experimentos y tomar decisiones
# Simulación de lanzar una moneda
resultado_moneda = random.choice(["Cara", "Cruz"])
print("Resultado del lanzamiento de la moneda:", resultado_moneda)

# Simulación de lanzar un dado
resultado_dado = random.randint(1, 6)
print("Resultado del lanzamiento del dado:", resultado_dado)

# Toma de decisión basada en un número aleatorio
if random.random() < 0.5:
    print("Toma la decisión A")
else:
    print("Toma la decisión B")

