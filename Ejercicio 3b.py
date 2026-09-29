# 3. Análisis y construcción de patrones. 

import re
print("---")
print("Patrones de validación")
print("---")

print("A) Un código formado por dos letras mayúsculas y cuatro números.")
patron_a = r"^[A-Z]{2}[0-9]{4}$"
texto_a = "AB1234"
print(re.findall(patron_a, texto_a))
print("---")


print("B) Legajo de exactamente cinco dígitos.")
patron_b = r"^[0-9]{5}$"
texto_b = "45892"
print(re.findall(patron_b, texto_b))
print("---")


print("C) Importe formado por el símbolo $ y uno o más dígitos")
patron_c = r"^\$[0-9]+$"
texto_c = "$1500"
print(re.findall(patron_c, texto_c))
print("---")


print("D) Palabra que comience con mayúscula y continúe únicamente con letras")
patron_d = r"^[A-Z][a-z]+$"
texto_d = "Python"
print(re.findall(patron_d, texto_d))
print("---")


print("E) Fecha con formato DD/MM/AAAA (solo forma)")
patron_e = r"^[0-9]{2}/[0-9]{2}/[0-9]{4}$"
texto_e = "25/12/2024"
print(re.findall(patron_e, texto_e))
print("---")