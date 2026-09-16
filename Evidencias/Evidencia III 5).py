# Evidencia III → Cadena de caracteres

texto = "Programacion en Python"

# A) → mostrar el primer y último caracter.

print("―――")
print(texto[0], texto[21]) # o -1
print("―――")

# B) → obtener la palabra "Programación" mediante slicing.
print("―――")
print(texto[0:12])
print("―――")

# C) → verificar si la palabra "Python" pertenece a la cadena.

if "Python" in texto:
    print("―――")
    print("Pertenece a la cadena.")
    print("―――")

else: 
    print("―――")
    print("No pertenece a la cadena.")
    print("―――")
    
# D) → Intentar modificar texto[0] y explicar el error obtenido.

texto[0]= "Programación en JavaScript"

