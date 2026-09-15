# Ejemplos de funciones Lambda


def duplicar1(numero):
    return numero * 2
print(duplicar1(5))

# versión lambda
duplicar2 = lambda numero: numero * 2
print(duplicar2(5))


sumar = lambda numero1, numero2: numero1 + numero2
resultado = sumar(4, 6)
print(resultado)


lambda numero1, numero2: numero1 + numero2


potencia = lambda base, exponente: base ** exponente
resultado = potencia(2, 3)
print(resultado)