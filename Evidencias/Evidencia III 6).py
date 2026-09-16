# Funciones y métodos de cadenas.
# A) texto.upper() 
# B) texto.lower() 
# C) texto.title()
# D) texto.capitalize()
# E) texto.replace("Python", "IA")
# F) texto.count("a")
# G) texto.find("Python")
# H) len(texto)

texto = "Programación I: clase 3"

print("---")
print("A)", texto.upper())
print("---")
print("B)", texto.lower())
print("---")
print("C)", texto.title())
print("---")
print("D)", texto.capitalize())
print("---")

texto = "Me gusta programar usando Python"

print("E)", texto.replace("Python", "IA"))
print("---")
print("F)", texto.count("a"))
print("---")
print("G)", texto.find("Python"))
print("---")
print("H)", len(texto))
print("---")

# Analicen, además los métodos de validación con las cadenas "Programación", "2026", "Python3" y "Programación en Python": 
# isalpha(), isdigit() e isalnum(). 
# Expliquen por qué isalpha() retorna False cuando la cadena contiene espacios, aunque todas sus palabras están formadas por 
# letras.

cadena1 = "Programación" 
cadena2 = "2026" 
cadena3 = "Python3" 
cadena4 = "Programación en python"

print("---")
print(f"\033[4m{cadena1}\033[0m") #subrayado
print("isalpha():", cadena1.isalpha())
print("isdigit():", cadena1.isdigit())
print("isalnum():", cadena1.isalnum())

print("---")
print(f"\033[4m{cadena2}\033[0m")
print("isalpha():", cadena2.isalpha())
print("isdigit():", cadena2.isdigit())
print("isalnum():", cadena2.isalnum())

print("---")
print(f"\033[4m{cadena3}\033[0m")
print("isalpha():", cadena3.isalpha())
print("isdigit():", cadena3.isdigit())
print("isalnum():", cadena3.isalnum())

print("---")
print(f"\033[4m{cadena4}\033[0m")
print("isalpha():", cadena4.isalpha())
print("isdigit():", cadena4.isdigit())
print("isalnum():", cadena4.isalnum())
print("---")