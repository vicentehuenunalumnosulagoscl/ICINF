notas = []
while True:
    entrada = input("Ingrese una nota o pulsa '0' para finalizar: ")
    if entrada == '0':
        break
    try:
        nota = float(entrada)
        notas.append(nota)
    except ValueError:
        print("ingrese un número válido o pulsa '0' para finalizar ")

if notas:
    CantidadNotas = len(notas)
    PromedioNotas = sum(notas) / CantidadNotas
    NotaMinima = min(notas)
    NotaMaxima = max(notas)

    print("Cantidad de notas:", CantidadNotas)
    print("Promedio de notas:", round(PromedioNotas, 2))
    print("Nota minima:", NotaMinima)
    print("Nota máxima:", NotaMaxima)
else:
    print("No se ingresaron notas")
