# Implementen la función es primo(número) utilizando una variable lógica y break. 
# La función deberá retornar False para todo número menor que 2 y detener la búsqueda apenas encuentre un divisor.
# a) Prueben la función con -3, 0, 1, 2, 9, 17 y 25.
# b) Indiquen en qué caso se ejecuta el break.
# c) Expliquen por qué pueden evitar iteraciones innecesarias.
# d) Comparen el resultado con una versión que recorra todos los posibles divisores

def es_primo(numero):
    if numero < 2:
        return False
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
            break
    return es_primo


def es_primo_sin_break(numero):
    if numero < 2:
        return False

    es_primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False

    return es_primo


# Programa principal

print(es_primo(-3))
print(es_primo(0))
print(es_primo(1))
print(es_primo(2))
print(es_primo(9))
print(es_primo(17))
print(es_primo(25))

