def solicitar_frase():
    frase = input("Ingrese una frase: ")
    while frase.strip() == "":
        print("la frase no puede estar vacía ni contener solamente espacios.")
        frase = input("ingrese una frase nuevamente: ")
    return frase


def normalizar_frase(frase):
    frase_normalizada = frase.lower()
    print(f'a) → frase normalizada: {frase_normalizada}')
    return frase_normalizada


def eliminar_caracteres(frase):
    frase_sin_signos = (
        frase.replace(".", "")
        .replace(",", "")
        .replace(";", "")
        .replace(":", "")
        .replace("?", "")
        .replace("¿", "")
        .replace("!", "")
        .replace("¡", "")
        .replace("+", "")
        .replace("-", "")
        .replace(".", "")
    )
    print(f'b) → fase sin signos: {frase_sin_signos}')
    return frase_sin_signos


def separar_palabras(frase):
    palabras = frase.split()
    print(f'c) → palabras: {palabras}')
    return palabras


def crear_conjunto(palabras):
    conjunto_palabras = set(palabras)
    print(f'd) → palabras diferentes: {conjunto_palabras}')
    return conjunto_palabras


def crear_frecuencias(palabras):
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    print(f'e) → diccionario de frecuencias: {frecuencias}')
    return frecuencias


def mostrar_orden_alfabetico(conjunto_palabras):
    palabras_ordenadas = sorted(conjunto_palabras)
    print('f) → palabras sin repetir en orden alfabético:')
    for palabra in palabras_ordenadas:
        print(f' {palabra}')

def mostrar_frecuencias(frecuencias):
    print("g) → frecuencia de cada palabra:")
    for palabra, frecuencia in frecuencias.items():
        print(f'{palabra}: {frecuencia}')


def mostrar_mas_frecuente(frecuencias):
    if len(frecuencias) > 0:
        palabra_mas_frecuente = max(frecuencias, key=frecuencias.get)
        frecuencia = frecuencias[palabra_mas_frecuente]
        print(f'h) → palabra más frecuente: {palabra_mas_frecuente}')
        print(f'aparece {frecuencia} veces.')
    else:
        print("no se ingresaron palabras.")





