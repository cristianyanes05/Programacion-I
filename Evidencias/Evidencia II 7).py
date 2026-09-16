# A) Cuadrado → retorna el cuadrado de un número

cuadrado = lambda x: x**2

print (cuadrado(4))
print (cuadrado(5))
print (cuadrado(144))

# B) es_par → retorna True cuando el número es par

es_par = lambda x: x % 2 == 0

print (es_par(17))
print (es_par(6))

# C) mayor → retorna el mayor entre dos números

mayor = lambda a, b: a if a > b else b

print (mayor(14, 52))
print (mayor(44, 12))
print (mayor (1,-15))

# D) aplicar_descuento → aplica un descuento porcentual a un precio. 

aplicar_descuento = lambda precio, descuento: precio * ((100 - descuento) / 100)

