def Ingresar_Puntajes():
    Puntajes = []
    for dia in range(1, 16):
        Puntaje = input("Ingrese el puntaje del dia " + str(dia) + " (entre 1 y 100): ")
        while not Puntaje.isdigit() or not (1 <= int(Puntaje) <= 100):
            print("El puntaje debe ser un número entero entre 1 y 100 ")
            Puntaje = input("Ingrese el puntaje del día " + str(dia) + " (entre 1 y 100): ")
        Puntajes.append(int(Puntaje))
    return Puntajes

def Dias_puntaje_bajo(Puntajes):
    Dias_bajos = []
    for dia, Puntaje in enumerate(Puntajes, start=1):
        if Puntaje < 60:
            Dias_bajos.append(dia)
    return Dias_bajos

print("Plataforma de evaluación de curso de 15 dias")

Puntajes = Ingresar_Puntajes()

Dias_bajos = Dias_puntaje_bajo(Puntajes)

if Dias_bajos:
    res = "Los días con puntaje menor a 60 puntos son: "
    for i, dia in enumerate(Dias_bajos):
        if i > 0:
            res += ", "
        res += "día " + str(dia)
    print(res)
else:
    print("No hay días con puntaje menor a 60 puntos.")
