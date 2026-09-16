
def calcular_importe(cantidad, precio):
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    if precio <= 0:
        raise ValueError("El precio debe ser mayor que cero")

    return cantidad * precio



while True:
    codigo = input("Ingrese el código del producto (FIN para terminar): ")

    if codigo == "FIN":
        break

    descripcion = input("Ingrese la descripción: ")

    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingres
        print("Error:", error)

cantidad_productos = len(productos)

if cantidad_productos == 0:
    print("No se cargaron productos")
else:
    importe_total = 0
    suma_precios = 0

    for producto in productos:
        importe = calcular_importe(producto[2], producto[3])
        importe_total = importe_total + importe
        suma_precios = suma_precios + producto[3]

    precio_promedio = suma_precios / cantidad_productos

    print("Cantidad de productos:", cantidad_productos)
    print("Importe total:", importe_total)
    print("Precio promedio:", precio_promedio)