import re 

print("---")
print("Funciones de metacaracteres")

print("---")
texto_a = "Hola mundo"

print("A) Anclas")
print("inicio (^):", re.findall(r"^Hola", texto_a))
print("final ($):", re.findall(r"mundo$", texto_a))
print("---")

texto_b = "gato gota g3to"

print("B) Comodín")
print("Comodín (.):", re.findall(r"g.to", texto_b))
print("---")

texto_c = "Código A-12"

print("C) Clases de caracteres")
print("Rangos ([A-Z] y [0-9]):", re.findall(r"[A-Z]-[0-9]", texto_c))
print("---")

texto_d = "100% Ok"

print("D) Negación")
print("No dígitos ([^0-9]):", re.findall(r"[^0-9]+", texto_d))
print("---")

texto_ef = "Llega en septiembre o setiembre"

print("F) Alternativas y Agrupación")
print("Palabras alternativas:", re.findall(r"(septiembre|setiembre)", texto_ef))
print("---")

texto_g = "color colour coluuour"

print("G) Repeticiones (?, *, +)")
print("Opcional (?):", re.findall(r"colou?r", texto_g)) # u opcional
print("Una o más (+):", re.findall(r"colu+or", texto_g)) # u una o más veces
print("---")

texto_h = "Tel: 1234-5678"

print("H) Especificación de repeticiones")
print("Exactas {4}:", re.findall(r"[0-9]{4}", texto_h))
print("---")

texto_i = "El total es $1000"

print("I) Escape de metacaracteres")
print("Buscar símbolo $ literal:", re.findall(r"\$[0-9]+", texto_i))
print("---")