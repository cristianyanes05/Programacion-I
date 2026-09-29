# Indiquen qué formato representa cada expresión y propongan dos datos válidos y dos inválidos:

import re 
print("---")
print("Representación de formatos")

print("---")
patron1 = r"^PROG[0-9]{3}$"
print("1) r\"^PROG[0-9]{3}$\" → representa un patrón que empieza con PROG seguido de exactamente 3 números.")
print("válido 1:", re.findall(patron1, "PROG123"))
print("válido 2:", re.findall(patron1, "PROG001"))
print("---")
print("inválido 1 (minúsculas):", re.findall(patron1, "prog123"))
print("inválido 2 (faltan dígitos):", re.findall(patron1, "PROG12"))
print("---")


patron2 = r"^[A-Za-z]{3,10}$"
print("2) r\"^[A-Za-z]{3,10}$\" → representa un patrón de letras de entre 3 y 10 caracteres.")
print("válido:", re.findall(patron2, "hola"))
print("válido:", re.findall(patron2, "python"))
print("---")
print("inválido: (menos de 3 letras):", re.findall(patron2, "so"))
print("inválido: (más de 10 letras):", re.findall(patron2, "programacionweb"))
print("---")


patron3 = r"^[0-9]{4}-[0-9]{4}$"
print("3) r\"^[0-9]{4}-[0-9]{4}$\" → representa: dos bloques de 4 números separados por un guión.")
print("válido:", re.findall(patron3, "1234-5678"))
print("válido:", re.findall(patron3, "0000-9999"))
print("---")
print("inválido: (bloque incompleto):", re.findall(patron3, "123-4567"))
print("inválido: (bloque sin guión):", re.findall(patron3, "12345678"))
print("---")


patron4 = r"^([A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2})$"
print("4) r\"^([A-Z]{3}[0-9]{3}|[A-Z]{2}[0-9]{3}[A-Z]{2})$\" → representa un patrón formato de 3 letras y 3 números o 2 letras, 3 números y 2 letras.")
print("válido 1:", re.findall(patron4, "ABC123"))
print("válido 2:", re.findall(patron4, "AB123CD"))
print("---")
print("inválido (minúsculas):", re.findall(patron4, "abc123"))
print("inválido (formato incorrecto):", re.findall(patron4, "AB1234C"))
print("---")