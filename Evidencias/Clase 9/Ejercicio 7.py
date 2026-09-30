# 7. Recorridos de diccionarios

stock = {
 "teclado": 12,
 "mouse": 20,
 "monitor": 7,
 "webcam": 5
}

print("a) recorrer el diccionario y mostrar sus claves")
for clave in stock:
    print(f'claves: {clave}')
print("---")
print(f'b) mostrar las cantidades mediante values(): {list(stock.values())}') #agregar el list fuera para evitar dict_values (view object)
print("---")
print(f'c) Mostrar cada producto y su stock mediante items(): {list(stock.items())}.')
print("---")
print(f'd) informar la cantidad de productos diferentes con len(): {len(stock)} ')
print("---")
total_unidades=sum(stock.values())
print(f'e) calcular el total de unidades disponibles: {total_unidades} ')
print("---")
producto_mayor_stock=max(stock, key=stock.get)
cantidad_mayor_unidades = stock[producto_mayor_stock]
print(f'f) informar el producto con mayor stock: el producto es {producto_mayor_stock} que cuenta con {cantidad_mayor_unidades} unidades')
print("---")


