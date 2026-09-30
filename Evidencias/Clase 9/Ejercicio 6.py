# 6. Acceso, alta, modificación y eliminación
# Utilizando el diccionario alumnos, resolver:
alumnos = {
           1001: "Ana",
           1002: "Bruno",
           1003: "Carla"
          }

print("---")
print(f"a) → mostrar el nombre (valor) asociado al legajo 1002: {alumnos[1002]}")
print("---")

# b) 
alumnos[1004] = "Teo"
alumnos[1001] = "Luciana"
print(f"b) → agregar el legajo 1004 y modificar el nombre (valor) asociado al legajo 1001: {alumnos}")
print("---")
print("c) verificar con in si existe el legajo 1010:")
if 1010 in alumnos:
  print("legajo encontrado")
else:
  print("no se ha encontrado el legajo")
print("---")
resultado_get = alumnos.get(1010, "no se ha encontrado el legajo 1010")
print(f"d) consultar con get() y un mensaje alternativo si no existe: {resultado_get}")
print("---")
if 1003 in alumnos:
    del alumnos[1003]
print(f'f) → eliminar un legajo inexistente con del, luego comprobar su existencia {alumnos}')
print("---")



