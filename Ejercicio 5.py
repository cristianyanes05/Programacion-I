# 5. findall y finditer
# Dado un texto con nombres, correos electrónicos, números de teléfono y códigos de productos:
# a) Utilicen re.findall() para obtener todas las secuencias numéricas.
# b) Utilicen re.finditer() para recorrer todas las coincidencias e informar contenido, posición inicial y final.
# c) Comparen el tipo de resultado que devuelve cada método.
# d) Prueben un patrón con grupos de captura y observen que findall() puede devolver tuplas en lugar de la coincidencia completa.
import re

texto = "nombre: cristian, correo electrónico: cris.yanes05@gmail.com, tel: 1155443322, código: BCHJA-987"
print("---")
print("a) Secuencias numéricas)")
patronA = r"[0-9]+"
res_findall = re.findall(patronA, texto)
print("resultado:", res_findall)
print("---")

print("b) recorrer secuencias")
res_finditer = re.finditer(patronA, texto)
for i in res_finditer:
    print("contenido:", i.group(), "inicio:", i.start(), "fin:", i.end())
print("---")

print("c) comparación de resultados")
print("findall → devuelve una lista:", type(res_findall))
print("finditer devuelve un iterador de objetos match:", type(res_finditer))
print("---")

patron_grupos = r"([a-z]+)-([0-9]+)"
texto_grupos = "producto-123 item-456"
res_grupos = re.findall(patron_grupos, texto_grupos)
print("d) findall() con grupos de captura:")
print("resultado (devuelve tuplas):", res_grupos)
print("---")