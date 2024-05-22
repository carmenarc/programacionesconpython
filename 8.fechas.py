import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Obtener la fecha actual
fecha_actual = datetime.date.today()

# Crear una fecha específica
fecha_especifica = datetime.date(2023, 5, 15)

# Imprimir la fecha y hora actual
print("Fecha y hora actual:", fecha_hora_actual)

# Imprimir la fecha actual
print("Fecha actual:", fecha_actual)

# Imprimir una fecha específica
print("Fecha específica:", fecha_especifica)

# Operaciones con fechas
# Sumar un día a la fecha actual
nueva_fecha = fecha_actual + datetime.timedelta(days=1)
print("Fecha actual + 1 día:", nueva_fecha)

# Restar un día a la fecha actual
nueva_fecha = fecha_actual - datetime.timedelta(days=1)
print("Fecha actual - 1 día:", nueva_fecha)

# Calcular la diferencia de días entre dos fechas
otra_fecha = datetime.date(2023, 5, 10)
diferencia = fecha_especifica - otra_fecha
print("Diferencia de días entre", fecha_especifica, "y", otra_fecha, ":", diferencia.days)
