# Una biblioteca posee 4 sucursales y registra la recaudación por multas durante 7 días. 
# Representen la información mediante una matriz de 4 filas y 7 columnas: cada fila corresponde a una sucursal y 
# cada columna a un día.
# Creen la matriz con filas independientes. Eviten duplicar una lista completa, porque todas las filas podrían referenciar 
# el mismo objeto.


# Crear una matriz de 4 filas y 7 columnas
matriz = [[0 for columna in range(7)] for fila in range(4)]


# a) Cargar las recaudaciones
for fila in range(4):
    for columna in range(7):
        recaudacion = int(input("Ingrese la recaudación obtenida: "))

        while recaudacion < 0:
            print("La recaudación no puede ser negativa.")
            recaudacion = int(input("Ingrese nuevamente la recaudación: "))

        matriz[fila][columna] = recaudacion


# b) Recaudación total de cada sucursal
for fila in range(4):
    total_sucursal = 0

    for columna in range(7):
        total_sucursal = total_sucursal + matriz[fila][columna]

    print("Recaudación total de la sucursal", fila + 1, ":", total_sucursal)


# c) Recaudación total de cada día
for columna in range(7):
    total_dia = 0

    for fila in range(4):
        total_dia = total_dia + matriz[fila][columna]

    print("Recaudación total del día", columna + 1, ":", total_dia)


# d) Recaudación general
recaudacion_general = 0

for fila in range(4):
    for columna in range(7):
        recaudacion_general = recaudacion_general + matriz[fila][columna]

print("Recaudación general:", recaudacion_general)


# e) Día con mayor recaudación
mayor_recaudacion = 0
dia_mayor_recaudacion = 0

for columna in range(7):
    total_dia = 0

    for fila in range(4):
        total_dia = total_dia + matriz[fila][columna]

    if total_dia > mayor_recaudacion:
        mayor_recaudacion = total_dia
        dia_mayor_recaudacion = columna + 1

print("El día con mayor recaudación fue el día",
      dia_mayor_recaudacion,
      "con $",
      mayor_recaudacion)