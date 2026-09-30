# 2. Pertenencia y operaciones entre conjuntos: resolver e interpretar cada resultado.
# a) Unión: grupo_a | grupo_b.
# b) Intersección: grupo_a & grupo_b.
# c) Diferencia: grupo_a - grupo_b y grupo_b - grupo_a.
# d) Diferencia simétrica: grupo_a ^ grupo_b.
# e) Pertenencia: 103 in grupo_a y 108 not in grupo_b.
# f) Explicar por qué la diferencia no es una operación conmutativa.
grupo_a = {101, 102, 103, 104, 105}
grupo_b = {104, 105, 106, 107}
# a)
print("---")
print(f'la union junta elementos de ambos conjuntos, si se repite algún elemento aparece una vez → {grupo_a | grupo_b}')
print("---")
print(f'la intersección toma solamente los elementos que estan en ambos conjuntos → {grupo_a & grupo_b}')
print("---")
print(f'la diferencia toma solamente los elementos que están en el primer conjunto pero no en el segundo conjunto comparado → {grupo_a - grupo_b}, {grupo_b - grupo_a}')
print("---")
print(f'la diferencia simetrica compara dos conjuntos para unirlos y quitar elementos que tengan en común → {grupo_a^grupo_b}')
print("---")
print("la pertenencia sirve para constatar si un elemento se encuentra dentro del conjunto con in/not in → 103 en el conjunto a:", 103 in grupo_a, "108 en el conjunto b:", 108 in grupo_b)
print("---")
print("porque el orden altera los resultados al igual que en una resta de números")
print("---")
conjunto_c = {"teo", "cristian", "joaquin", "@", 17}
conjunto_d = {"teo", "cristian", "joaquin", "@", 17}
print(f'la diferencia comun y simétrica devuelven conjuntos vacíos si tienen los mismos elementos: {conjunto_c - conjunto_d} {conjunto_c ^ conjunto_d}')
print("---")