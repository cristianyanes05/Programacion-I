import re

texto="cyanesdelisio@uade.edu.ar, cris.yanes05@gmail.com, 7548-9456, 1234-9874, PE1555, BA4732, hola, python.com, 17"

# patrones que utilice para cada dato de identificacion
patron_correo= r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
patron_telefono = r"[0-9]{4}-[0-9]{4}"
patron_codigo = r"[A-Z]{2}[0-9]{4}"

correos = re.findall(patron_correo, texto)
telefonos = re.findall(patron_telefono, texto)
codigos = re.findall(patron_codigo, texto)

print("\t")
print("a) coincidencias encontradas de cada tipo:")
print(f"correos: {re.findall(patron_correo, texto)}")
print(f"teléfonos: {re.findall(patron_telefono, texto)}")
print(f"códigos: {re.findall(patron_codigo, texto)}")
print("\t")

print("b) cantidad de coincidencias encontradas:")
print(f"cantidad de correos: {len(re.findall(patron_correo, texto))}")
print(f"cantidad de teléfonos: {len(re.findall(patron_telefono, texto))}")
print(f"cantidad de códigos: {len(re.findall(patron_codigo, texto))}")
print("\t")

print("c) posicion inicial y final de cada dato del texto")

for match in re.finditer(patron_correo, texto):
    print("correo electrónico encontrado:", match.group())
    print("posiciones: inicio =", match.start(), "fin =", match.end())
    print("----")

for match in re.finditer(patron_telefono, texto):
    print("teléfono encontrado:", match.group())
    print("posiciones: inicio =", match.start(), "fin =", match.end())
    print("----")

for match in re.finditer(patron_codigo, texto):
    print("código encontrado:", match.group())
    print("posiciones: inicio =", match.start(), "fin =", match.end())
    print("\t")