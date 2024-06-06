nombres = []
for i in range(7):
    nombre = input("Ingrese el nombre de la persona " + str(i + 1) + ": ")
    nombres.append(nombre)

nombresConA = []
for nombre in nombres:
    if nombre[-1] == "a":  
        nombresConA.append(nombre)

print("Lista de nombres que terminan con 'a':")
print(nombresConA)
