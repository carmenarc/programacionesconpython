from enum import Enum, auto

# Definir un enumerado para los días de la semana
class DiasSemana(Enum):
    LUNES = auto()
    MARTES = auto()
    MIERCOLES = auto()
    JUEVES = auto()
    VIERNES = auto()
    SABADO = auto()
    DOMINGO = auto()

# Imprimir los nombres de los días de la semana
print("Los días de la semana son:")
for dia in DiasSemana:
    print(dia.name)
