# 5. Primer contacto con los diccionarios (dict)

alumnos = {
 1001: "Ana",
 1002: "Bruno",
 1003: "Carla"
}

diccionario_vacio = {}
conjunto_vacio = set()

print("---")
print(f'a) → en este diccionario, cada clave representa un código inmutable la cual permite acceder a un alumno en particular (valor) → {alumnos}')
alumnos[1002]="teo"
print("---")
print(f'b) → que ocurre si se le vuelve a asignar un valor a la clave 1002: {alumnos} → el valor se reemplaza')
print("---")
print('c) → porque una lista no puede utilizarse como clave: Las claves deben pertenecer a un tipo inmutable: números, cadenas o tuplas.')
print("---")
print(f'd) → las llaves vacías indican la creación de un diccionario: {diccionario_vacio}, en cambio set() se utiliza para crear un conjunto: {conjunto_vacio}')
print("---")