def ingresar_nombres():
    nombres = []
    for i in range(7):
        nombre = input("Ingrese el nombre de la persona " + str(i + 1) + ": ")
        nombres.append(nombre)
    return nombres

def EliminarNombresSinA(nombres):
    NombresConA = []
    for nombre in nombres:
        if nombre[-1] == "a":
            NombresConA.append(nombre)
    return NombresConA


print("Ingreso de 7 nombres de personas")

nombres = ingresar_nombres()

NombresConA = EliminarNombresSinA(nombres)

print("Lista de nombres que terminan con 'a':")
print(NombresConA)
