def convierteNegativo(lista):
    return [-num for num in lista]

lista = []
print("Ingrese 10 numeros positivos")

for i in range(10):
    num = input("Ingrese el número " + str(i + 1) + ": ")
    while not num.isdigit() or int(num) <= 0:
        print("Eso no es un número positivo. Inténtalo de nuevo.")
        num = input("Ingrese el número " + str(i + 1) + ": ")
    lista.append(int(num))

listaNegativa = convierteNegativo(lista)
print("Lista de numeros convertidos en negativo: " + str(listaNegativa))
