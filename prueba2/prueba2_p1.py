notas = []
while True:
    entrada = input("Ingrese una nota o pulse '0' para finalizar: ")
    if entrada == '0':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 7: 
            notas.append(nota)
        else:
            print("Ingrese una nota entre 1 y 7 o pulse '0' para finalizar.")
    except ValueError:
        print("Ingrese un número valido o pulse '0' para finalizar.")

if notas:
    cantidadNotas = len(notas)
    promedioNotas = sum(notas) / cantidadNotas
    notaMinima = min(notas)
    notaMaxima = max(notas)

    print("Cantidad de notas:", cantidadNotas)
    print("Promedio de notas:", round(promedioNotas, 2))
    print("Nota mínima:", notaMinima)
    print("Nota máxima:", notaMaxima)
else:
    print("No se ingresaron notas.")
