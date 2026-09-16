# Una biblioteca universitaria cobra una multa de $800 por cada día de atraso. 
# Si el libro fue devuelto con al menos un día de atraso y estaba reservado por otra persona, se agrega un cargo fijo de $2500.
# La cantidad de días no puede ser negativa.

dias= int(input("Ingrese la cantidad de días de atraso: "))

reservado= input("¿El libro estaba reservado por otra persona? (si/no): ")

multa = dias * 800

if dias >= 1 and reservado == "si":
    multa = multa + 2500

while dias < 0:
    print ("La cantidad de días de atraso no puede ser menor a 0")  
    dias = int(input("Reingrese la cantidad de días de atraso: "))

print("Total a abonar: $", multa)