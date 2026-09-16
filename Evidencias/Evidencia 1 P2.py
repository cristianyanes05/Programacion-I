# Una biblioteca universitaria cobra una multa de $800 por cada día de atraso. 
# Si el libro fue devuelto con al menos un día de atraso y estaba reservado por otra persona, se agrega un cargo fijo de $2500.
# La cantidad de días no puede ser negativa.

def calcular_multa(dias_atraso, reservado):
    monto = dias_atraso * 800
    
    if dias_atraso >= 1 and reservado:
        multa = multa + 2500
    
    return multa  


def mostrar_resultado (resultado):
    print ("Multa a abonar: ", resultado)

print ("---Programa principal---")

dias = int(input("Ingrese la cantidad de días de atraso: "))
respuesta = (input("¿El libro ya se encontraba reservado? (S/N): "))

if respuesta == "S": # S tiene que ir entre comillas pq sino es variable no definida
    reservado = True
else:
    reservado = False
    
multa = calcular_multa(dias, reservado)

mostrar_resultado (multa)





