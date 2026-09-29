import re 

patron_nombre= r"[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+"
patron_legajo = r"[0-9]{7}"  
patron_correo= r"[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
patron_telefono= r"[0-9]{10}"
patron_comision= r"[A-Z]{2}[0-9]{4}"

# a)
def validar_nombre (nombre):
    return re.fullmatch(patron_nombre, nombre) 

def validar_legajo(legajo):
    return re.fullmatch(patron_legajo, legajo) 

def validar_correo(correo):
    return re.fullmatch(patron_correo, correo) 
def validar_telefono(telefono):
    return re.fullmatch(patron_telefono, telefono) 

def validar_comision(comision):
    return re.fullmatch(patron_comision, comision) 

#b)
def mostrar_msj_error(mensaje):
    print(f"Error: {mensaje}")
    

# salida de datos 

def mostrar_resultados(nombre, legajo, correo, telefono, comision):
    print("\n")
    print("Registro exitoso.")
    print(f"nombre:{nombre}")
    print(f"negajo:{legajo}")
    print(f"correo:{correo}")
    print(f"teléfono:{telefono}")
    print(f"comisión:{comision}")


