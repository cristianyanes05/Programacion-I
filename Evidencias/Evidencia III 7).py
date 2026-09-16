# Conversión de tipos y formateo.
# Desarrollen un programa que solicite nombre del producto, precio unitario y cantidad. 
# El precio deberá convertirse a float y la cantidad a int. Luego calculen el importe total.

print("---")
producto = input("Ingrese el nombre del producto: ")
print("---")
precio_unitario = float(input("Ingrese el precio del producto: "))
print("---")
cantidad_producto = int(input("Ingrese la cantidad a adquirir: "))
print("---")
importe_total = precio_unitario * cantidad_producto

# Muestren el resultado de dos maneras:
# A) Utilizando una f-string y formato de dos decimales.
# B) Utilizando concatenación; conviertan explícitamente los valores numéricos con str().

print(" ---RESULTADOS---")
print("A)", f'Total a pagar: $ {importe_total:.2f}')
print("---")
print("B)", "Total a pagar: $" + str(round(importe_total, 2)))
print("---")





