palabras = []
while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if not palabra:
        break
    palabras.append(palabra)

longitudMasLarga = 0
for palabra in palabras:
    contador = 0
    for _ in palabra:
        contador += 1
    if not longitudMasLarga or contador > longitudMasLarga:
        longitudMasLarga = contador

print(f"La palabra con la mayor cantidad de caracteres tiene: "+longitudMasLarga+" caracteres.")
