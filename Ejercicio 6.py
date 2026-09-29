# 6. 
# a) Utilizar re.sub() para reemplazar todos los teléfonos con formato 123-456-7890 por XXX-XXX-XXXX.
# b) Utilizar re.split() para dividir un texto usando puntos, comas, signos de pregunta y espacios como separadores.
# c) Compilar un patrón mediante re.compile() y reutilizarlo con match(), findall() y sub().
# d) Explicar cuándo mejora la legibilidad compilar una expresión regular.

import re

print("\n--- ejercicio 6: sub, split y compile ---\n")


texto_tels = "teléfono: 123-456-7890"
patron_tel = r"[0-9]{3}-[0-9]{3}-[0-9]{4}"
resultado_sub = re.sub(patron_tel, "XXX-XXX-XXXX", texto_tels)

print("a) reemplazo de teléfonos")
print("texto original:", texto_tels)
print("resultado:", resultado_sub)
print("---")


texto_separar = "hola,cómo estás?todo bien.genial"
patron_sep = r"[,.? ]+"
resultado_split = re.split(patron_sep, texto_separar)

print("b) división con múltiples separadores")
print("texto original:", texto_separar)
print("resultado:", resultado_split)
print("---")


patron_anio = re.compile(r"[0-9]{4}")
fechas = "07/08/2017|03/02/1984|17/03/2001"

anios = patron_anio.findall(fechas)
match_ejemplo = patron_anio.match("2024")
sub_ejemplo = patron_anio.sub("AAAA", fechas)

print("c) patrón compilado reutilizado")
print("uso con findall():", anios)
print("uso con match():", match_ejemplo.group() if match_ejemplo else None)
print("uso con sub():", sub_ejemplo)
print("---")