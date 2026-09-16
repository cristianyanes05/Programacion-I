cantidad = 0
suma = 0

while True:
    numero = int(input("Ingrese un número (-1 para terminar): "))
    if numero == -1:
        break
    cantidad = cantidad + 1
    suma = suma + numero

if cantidad == 0:
    print("No existen datos para calcular el promedio")
else:
    promedio = suma / cantidad
    print("Cantidad:", cantidad)
    print("Suma:", suma)
    print("Promedio:", promedio)