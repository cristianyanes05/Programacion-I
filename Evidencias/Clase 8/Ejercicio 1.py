# Expresiones regulares: A) ¿Qué diferencia existe entre un patrón literal y uno que contiene metacaracteres?

import re

# Búsqueda de un patrón literal.

cadena1="Orientador VI → clase 8:(16/09)"
patron_buscar = "clase"

print ("---")
print("Búsqueda de un patrón literal:", re.findall(patron_buscar, cadena1), "→ devuelve la coincidencia exacta.")
print("---")

# Búsqueda de un patrón con metacaracteres.
patron_buscar2= ".a"
print("Busqueda de un patrón con metacaracteres:", re.findall(patron_buscar2, cadena1), "→ devuelve cualquier letra seguida del caracter a.")
print("---")

# B) ¿Qué significa encontrar una coincidencia/match?

cadena1= "Hola es un perro"
cadena2= "Papas fritas"
coincidencia_buscada = "perro"
coincidencia_buscada2 = ".uva"

print("Busqueda de un patron x coincidencia:", re.findall(coincidencia_buscada, cadena1), "→ hubo match")
print("---")
print("Busqueda de un patrón sin coincidencia:", re.findall(coincidencia_buscada2, cadena2), "→ no hubo match")
print("---")

# D) → ¿Por qué conviene escribir los patrones como cadenas crudas, por ejemplo r"[0-9]+"?

salario= "El salario es de $10.000"

patron= r"[0-9.]+"

print(re.findall(patron, salario), "→ Imprime solo el monto")



