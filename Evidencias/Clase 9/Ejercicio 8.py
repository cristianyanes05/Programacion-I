# 8. diccionarios con valores compuestos 

#Crear un diccionario cuya clave sea el nombre de un grupo y cuyo valor sea un conjunto con las tecnologías que utiliza. 
# Esta estructura combina dos niveles: el diccionario localiza al grupo y el conjunto evita tecnologías repetidas.

tecnologias_por_grupo = {
 "Grupo 1": {"Python", "Git"},
 "Grupo 2": {"Python", "JSON"}
}

tecnologias_por_grupo["Grupo 3"] = {"Html", "Css"} # si no uso llaves se crea una tupla dentro del conjunto
print("---")
print(f'a) → agregar un nuevo grupo al diccionario: {tecnologias_por_grupo}')
print("---")
tecnologias_por_grupo["Grupo 3"].add("javascript")
print(f'b) → incorporar una tecnología a un grupo existente: {tecnologias_por_grupo}')
print("---")
consultar_grupo=tecnologias_por_grupo.get("Grupo 3")
print(f'c) → consultar un grupo mediante get() sin provocar una excepción {consultar_grupo}')
print("---")
print(f'd) → recorrer el diccionario mostrando cada grupo y sus tecnologías')
for grupo in tecnologias_por_grupo:
    print(f'{grupo} {tecnologias_por_grupo[grupo]}')
print("---")