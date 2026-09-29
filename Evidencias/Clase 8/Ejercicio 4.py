# 4. match, search y fullmatch

import re 

print("---")

patron = r"[A-Za-z][0-9]{3}"
codigo = "A123XYZ"

print("patrón utilizado:", patron)
print("cadena evaluada:", codigo)
print("---")


inicio = re.match(patron, codigo)
print("a) re.match():", inicio)
print("explicación a: encuentra coincidencia porque evalúa solo el inicio de la cadena (las primeras 4 posiciones coinciden).")
print("---")


completo = re.fullmatch(patron, codigo)
print("b) re.fullmatch():", completo)
print("explicación b: devuelve none porque exige que la totalidad de la cadena coincida exactamente con el patrón.")
print("---")


frase = "el código es a123xyz para ingresar."
patron_num = r"[0-9]+"

resultado = re.search(patron_num, frase)

print("c y d) localización de primera secuencia numérica:")
print("frase evaluada:", frase)
if resultado is not None:
    print("coincidencia encontrada (group()):", resultado.group())
    print("posición inicial (start()):", resultado.start())
    print("posición final (end()):", resultado.end())
    print("rango completo (span()):", resultado.span())
else:
    print("no se encontró coincidencia.")

print("---")


cadena_ignore = "clave: A123XYZ"
patron_letras = r"a123"

resultado_ignore = re.search(patron_letras, cadena_ignore, re.IGNORECASE)

print("e) búsqueda con re.IGNORECASE:")
print("cadena evaluada:", cadena_ignore)
if resultado_ignore is not None:
    print("resultado de la búsqueda:", resultado_ignore.group())
    print("ubicación en texto (span()):", resultado_ignore.span())
else:
    print("no se encontró coincidencia.")

print("---")