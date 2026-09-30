# 9. Actividad integradora: análisis de una frase 
# Desarrollar un programa que solicite una frase y realice las siguientes tareas:

import funciones

frase_solicitada = funciones.solicitar_frase()
print("---")
frase_normalizada = funciones.normalizar_frase(frase_solicitada)
print("---")
frase_sin_signos = funciones.eliminar_caracteres(frase_normalizada)
print("---")
palabras = funciones.separar_palabras(frase_sin_signos)
print("---")
conjunto_palabras = funciones.crear_conjunto(palabras)
print("---")
frecuencias = funciones.crear_frecuencias(palabras)
print("---")
funciones.mostrar_orden_alfabetico(conjunto_palabras)
print("---")
funciones.mostrar_frecuencias(frecuencias)
print("---")
funciones.mostrar_mas_frecuente(frecuencias)
print("---")






