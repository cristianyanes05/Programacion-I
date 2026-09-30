# 4. Aplicación de conjuntos 
# Dada una lista de códigos de alumnos que puede contener repeticiones, desarrollen una función codigos_unicos(codigos) que retorne un conjunto 
# con los códigos diferentes.

codigos_alumnos= ["A03", "A07", "A048", "A056", "A017", "A046", "A03", "A07", "A056"]

def codigos_unicos(codigos):
    return set(codigos_alumnos) #set convierte a conjunto y elimina duplicados

def informar_distintos(conjunto):
    return len(conjunto)
   
resultado_unicos = codigos_unicos(codigos_alumnos)

def verificar_codigo(conjunto, codigo):
    return codigo in conjunto 

codigo_buscado= "105"

def convertir_conjunto_a_lista(conjunto):
    return sorted(conjunto) #sorted devuelve y ordena una lista de A a Z

def convertir_lista_a_conjunto(lista):
    return set(lista)

print("---")
print(f'lista convertida a un conjunto con códigos diferentes: {codigos_unicos(codigos_alumnos)}')
print("---")
print(f'a) → cantidad de códigos distintos: {informar_distintos(resultado_unicos)}')
print("---")
print(f'b) → verificar si el código 105 fue informado: {verificar_codigo(codigos_alumnos, codigo_buscado)}')
print("---")
print(f'c) → Conviertan el conjunto en una lista ordenada para mostrar un resultado predecible: {convertir_conjunto_a_lista(resultado_unicos)}') 
print("---")
print(f'd) → ¿que info. se pierde al convertir una lista en conjunto? {convertir_lista_a_conjunto(codigos_alumnos)}')
print("1º se pierde la info. de elementos duplicados, 2º se pierde el orden original de los elementos")
print("---")
