PreciosDolares = []
print("Ingrese 10 precios de productos en dolares: ")
for i in range(10):
    while True:
        entrada = input("Precio " + str(i + 1) + ": ")
        if entrada.replace('.', '', 1).lstrip('-').isdigit():
            precio = float(entrada)
            PreciosDolares.append(precio)
            break
        else:
            print("Ingrese un número valido. ")
PreciosPesos = [precio * 950 for precio in PreciosDolares]
print("Lista de precios en pesos chilenos:")
for i, precio in enumerate(PreciosPesos, start=1):
    print("Precio " + str(i) + ": $" + str(round(precio, 2)) + " CLP")
