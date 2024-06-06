puntajes = []
dia = 1
while dia <= 15:
    puntaje = input("Ingrese el puntaje del día " + str(dia) + " (entre 1 y 100): ")
    esEntero = puntaje.isdigit() and 1 <= int(puntaje) <= 100
    if esEntero:
        puntajes.append(int(puntaje))
        dia += 1
    else:
        print("El puntaje debe ser un número entero entre 1 y 100.")

diasBajos = []
dia = 1
while dia <= len(puntajes):
    puntaje = puntajes[dia - 1]
    if puntaje < 60:
        diasBajos.append(dia)
    dia += 1

if diasBajos:
    resultado = "Los días con puntaje menor a 60 puntos son: "
    primer_dia = True
    for dia in diasBajos:
        if not primer_dia:
            resultado += ", "
        resultado += "día " + str(dia)
        primer_dia = False
    print(resultado)
else:
    print("No hay días con puntaje menor a 60 puntos.")
("No hay días con puntaje menor a 60 puntos.")
