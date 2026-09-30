# 3. Métodos y relaciones entre conjuntos 

TECNOLOGIAS = {"playstation", "mouse", "parlante", "reloj"}

print("---")
agregar_tecno= TECNOLOGIAS.add("router")
print(f'a) → agregar un elemento al conjunto mediante .add {TECNOLOGIAS}')
print("---")
quitar_tecno= TECNOLOGIAS.remove("reloj")
print(f'b) → quitar un elemento del conjunto mediante .remove {TECNOLOGIAS}')
print("---")
print('c) → quitar un elemento inexistente mediante .remove provoca un error de tipo KeyError: remove exige su existencia')
print("---")
quitar_discard= TECNOLOGIAS.discard("auricular")
print(f'd) → nquitar un elemento inexistente con el método discard no sucede nada y continúa la ejecución normal: {quitar_discard}')
print("---")

tecnologias2= {"playstation", "mouse", "parlante", "reloj"}
tecnologias3= {"playstation", "mouse", "parlante", "reloj", "auricular"}

print(f"e) → verificación con issubset() si un conjunto tecnologías esta incluido dentro de otro (todos sus elementos están dentro de este otro): {tecnologias2.issubset(tecnologias3)}")
print("tambien se puede chequear con un if else")
if tecnologias2.issubset(tecnologias3):
  print("el conjunto tecnologias2 está incluido dentro del conjunto tecnologias3")
else:
  print("no está contenido")   
print("---")

print(f'f) → verificación con issuperset() la relación inversa: {tecnologias3.issuperset(tecnologias2)}')
print("---")
print("g) → vaciado de una copia del conjunto con clear() sin afectar al original:")
copia_a_vaciar = TECNOLOGIAS.copy()
copia_a_vaciar.clear()
print("---")
print(f'copia vaciada: {copia_a_vaciar} copia original: {TECNOLOGIAS} ')
print("---")


