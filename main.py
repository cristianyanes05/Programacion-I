import validaciones  # anteponer la leyenda validaciones antes del nombre de la función al haber importado de esta manera.

print("\t")
print("--¡Bienvenido al formulario de registro!--")
print("Para comenzar el registro, a continuación se le solicitarán los siguientes datos:")
print("\t")

# c)
nombre = input("Ingrese su nombre y su apellido (opcional): ")
while not validaciones.validar_nombre(nombre):
    validaciones.mostrar_msj_error("el nombre debe contener únicamente letras ")
    nombre = input("reingrese su nombre y su apellido (opcional): ")
print("nombre registrado.")


legajo = input("Ingrese su número de legajo: ")
while not validaciones.validar_legajo(legajo):
    validaciones.mostrar_msj_error("El legajo debe contener y estar formado por siete números.")
    legajo = input("reingrese su número de legajo: ")
print("legajo registrado")


correo = input("Ingrese su correo electrónico: ")
while not validaciones.validar_correo(correo):
      validaciones.mostrar_msj_error("Se solicita un correo de formato estándar.")
      correo=input("reingrese su correo electrónico: ")
print("correo registrado.")

telefono = input("ingrese su número de teléfono: ")
while not validaciones.validar_telefono(telefono):
    validaciones.mostrar_msj_error("se solicita un número de teléfono de diez dígitos")
    telefono=input("reingrese su número de teléfono: ")
print("Número de teléfono registrado.")


comision = input("Ingrese el código de comisión perteneciente: ")
while not validaciones.validar_comision(comision):
    validaciones.mostrar_msj_error("el código debe estar formado por dos letras mayúsculas y cuatro números")
    comision=input("reingrese el código de comisión perteneciente: ")
print("Comisión registrada.")  

validaciones.mostrar_resultados(nombre, legajo, correo, telefono, comision)
