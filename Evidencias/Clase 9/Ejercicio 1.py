# Responder: 
# a) ¿Por qué los valores repetidos aparecen una sola vez?
# b) ¿Por qué un conjunto vacío se crea con set() y no con {}?
# c) ¿Sería correcto intentar mostrar lenguajes[0]? Justifiquen.

lenguajes = {"Python", "Java", "C", "Python", "C"}

print("\n --------------------")
print(f"a) Porque debido a su estructura, un conjunto es una colección de elementos sin orden y sin duplicados. {lenguajes}")
print("---")

vacio1= {}
vacio2= set()

print(f"b) las llaves crean un diccionario ({type(vacio1)}), mientras que set() crea un conjunto ({type(vacio2)} ") 
print("---")

print("c) No, debido a que no es una secuencia:  sus elementos no se identifican mediante posiciones y, por lo tanto, no se accede a ellos con índices ni slicing.   ")
try:
    print(lenguajes[0])
except TypeError as error:
    print(f"el error es: {error}")
print("---")

