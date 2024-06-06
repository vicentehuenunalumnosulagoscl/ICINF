def IngresarPalabras():
    palabras = []
    while True:
        palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
        if palabra == "":
            break
        palabras.append(palabra)
    return palabras

def EncontrarPalabraMasLarga(palabras):
    if not palabras:
        return 0
    PalabraMasLarga = max(palabras, key=len)
    return len(PalabraMasLarga)

print("Ingreso de palabras. Presione Enter sin escribir nada para finalizar.")

palabras = IngresarPalabras()

LongitudMasLarga = EncontrarPalabraMasLarga(palabras)

print("La palabra con la mayor cantidad de caracteres tiene:", LongitudMasLarga, "caracteres.")
