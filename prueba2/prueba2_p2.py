preciosDolares = []
print("Ingrese 10 precios de productos en dólares: ")
for i in range(10):
    while True:
        entrada = input("Precio " + str(i + 1) + ": ")
        esValido = True
        for indice, caracter in enumerate(entrada):
            if not (caracter.isdigit() or caracter == '.' or (caracter == '-' and indice == 0)):
                esValido = False
                break

        if esValido:
            precio = float(entrada)
            preciosDolares.append(precio)
            break
        else:
            print("Ingrese un número válido. ")

preciosPesos = [precio * 950 for precio in preciosDolares]
print("Lista de precios en pesos chilenos:")
for i, precio in enumerate(preciosPesos, start=1):
    print("Precio " + str(i) + ": $" + str(round(precio, 2)) + " CLP")
