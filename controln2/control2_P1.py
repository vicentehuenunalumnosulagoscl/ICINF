def esEntero(cadena):
    return cadena.isdigit() and 1 <= int(cadena) <= 100


puntajes = []
for dia in range(1, 16):
    puntajeValido = False
    while not puntajeValido:
        puntaje = input("Ingrese el puntaje del dia " + str(dia) + " (entre 1 y 100): ")
        if esEntero(puntaje):
            puntajes.append(int(puntaje))
            puntajeValido = True
        else:
            print("El puntaje debe ser un número entero entre 1 y 100.")

diasBajos = []
for dia, puntaje in enumerate(puntajes, start=1):
    if puntaje < 60:
        diasBajos.append(dia)

if diasBajos:
    resultado = "Los días con puntaje menor a 60 puntos son: "
    for i, dia in enumerate(diasBajos):
        if i > 0:
            resultado += ", "
        resultado += "día " + str(dia)
    print(resultado)
else:
    print("No hay días con puntaje menor a 60 puntos.")
